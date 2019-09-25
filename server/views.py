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
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


class Login(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(Login, self).dispatch(*args, **kwargs)


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
        return ['us6.arexgo.com']


class Signup(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(Signup, self).dispatch(*args, **kwargs)

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
            'users': Voucher.objects.all(),
        }
        return HttpResponse(template.render(context, request))


class Form(View):
    def post(self, request):
        form = ProfileForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            ProfileComponent.objects.bulk_create([
                ProfileComponent(name=data['pct_name'], available_to_siblings=data['pct_available_to_siblings'],
                                 user_id=data['pct_user']),
                ProfileComponent(name=data['pcd_name'], available_to_siblings=data['pcd_available_to_siblings'],
                                 user_id=data['pcd_user']),
                ProfileComponent(name=data['p_name'], available_to_siblings=data['p_available_to_siblings'],
                                 user_id=data['p_user'])
            ])
            Profile(name=data['p_name'], available_to_siblings=data['p_available_to_siblings'],
                    user_id=data['p_user']).save()
            Radgroupcheck.objects.bulk_create([
                Radgroupcheck(groupname=data['d_groupname1'], attribute=data['d_attribute1'], op=data['d_op1'],
                              value=data['d_value1']),
                Radgroupcheck(groupname=data['d_groupname2'], attribute=data['d_attribute2'], op=data['d_op2'],
                              value=data['d_value2']),
                Radgroupcheck(groupname=data['d_groupname3'], attribute=data['d_attribute3'], op=data['d_op3'],
                              value=data['d_value3']),
                Radgroupcheck(groupname=data['t_groupname1'], attribute=data['t_attribute1'], op=data['t_op1'],
                              value=data['t_value1']),
                Radgroupcheck(groupname=data['t_groupname2'], attribute=data['t_attribute2'], op=data['t_op2'],
                              value=data['t_value2']),
                Radgroupcheck(groupname=data['t_groupname3'], attribute=data['t_attribute3'], op=data['t_op3'],
                              value=data['t_value3'])
            ])
            Radusergroup.objects.bulk_create([
                Radusergroup(username=data['rdg_username'], groupname=data['rdg_groupname'],
                             priority=data['rdg_priority']),
                Radusergroup(username=data['rdg_username2'], groupname=data['rdg_groupname2'],
                             priority=data['rdg_priority2'])
            ])

            return HttpResponseRedirect('/form')
        print('invalid form')
        return HttpResponseRedirect('/form')

    def get(self, request):
        form = ProfileForm()
        return render(request, 'form.html', {'form': form})