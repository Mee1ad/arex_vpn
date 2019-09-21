from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse
from server.models import *
import json
import pysnooper
from django.db import IntegrityError
import os
from time import time
from django.http import HttpResponseRedirect
from .form import ProfileForm
from django.template import loader


class Login(View):
    def post(self, request):
        data = json.loads(request.body)
        code = int(data['code'])
        websites = ApiHit.objects.all()
        websites = [item.url for item in websites]
        voucher = Voucher.objects.select_related('profile').filter(password=code + 1).first()
        if voucher is None:
            return JsonResponse({'message': 'ok'}, status=404)
        total_data = voucher.data_cap
        total_time = voucher.time_cap
        data_used = voucher.data_used
        time_used = voucher.time_cap - voucher.time_used
        data_remaining = voucher.data_cap - voucher.data_used
        time_remaining = voucher.time_used
        data_usage_percent = int(data_remaining / voucher.data_cap * 100)
        time_usage_percent = int(time_remaining / voucher.time_cap * 100)
        ping = self.ping_server()
        res = {'total_data': total_data, 'total_time': total_time, 'data_used': data_used, 'time_used': time_used,
               'data_remaining': data_remaining, 'time_remaining': time_remaining,
               'data_usage_percent': data_usage_percent, 'time_usage_percent': time_usage_percent,
               's': ping, 'urls': websites}
        return JsonResponse(res)

    def ping_server(self):
        servers = ['us1.arexgo.com', 'us2.arexgo.com', 'us3.arexgo.com', 'us4.arexgo.com', 'us5.arexgo.com',
                   'us6.arexgo.com']
        server_ping = {}
        # for server in servers:
        #     start = time()
        #     os.system(f'ping -n 1 {server}')
        #     latency = time() - start
        #     server_ping[server] = latency
        # pings = sorted(server_ping, key=server_ping.get)
        # return [pings[0], pings[1]]
        return 'us6.arexgo.com'


class Signup(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            ApiUser(pin=data['pin'], device_id=data['device-id'], device=data['device'], os=data['os'], ip=data['ip'],
                    mac=data['mac']).save()
            return JsonResponse({'message': 'ok'})
        except IntegrityError:
            return JsonResponse({'message': 'already signed up'})


class FormView(View):
    def get(self, request):
        template = loader.get_template('form.html')

        context = {
            'users': User.objects.all()[:3],
        }
        return HttpResponse(template.render(context, request))


class Form(View):
    def post(self, request):
        print(request.POST)
        form = ProfileForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponseRedirect('/form')
        print('invalid form')
        return HttpResponseRedirect('/form')

    def get(self, request):
        form = ProfileForm()
        return render(request, 'form.html', {'form': form})