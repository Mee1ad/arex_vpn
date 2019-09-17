from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse
from server.models import *
import json
import re
import jwt
import pysnooper
from django.utils import timezone
import random
from django.db import IntegrityError
import os
from time import time


class Login(View):
    @pysnooper.snoop()
    def post(self, request):
        data = json.loads(request.body)
        code = int(data['code'])
        ip = request.META.get('REMOTE_ADDR')
        print(ip)
        # device_id = data['device_id']
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
        res = {'total_data': total_data, 'total_time': total_time, 'data_used': data_used, 'time_used': time_used,
               'data_remaining': data_remaining, 'time_remaining': time_remaining,
               'data_usage_percent': data_usage_percent, 'time_usage_percent': time_usage_percent}
        return JsonResponse(res)


class Ping(View):
    def get(self, request):
        servers = ['us1.arexgo.com', 'us2.arexgo.com', 'us3.arexgo.com', 'us4.arexgo.com', 'us5.arexgo.com',
                   'us6.arexgo.com']
        server_ping = {}
        for server in servers:
            start = time()
            os.system(f'ping -n 1 {server}')
            latency = time() - start
            server_ping[server] = latency
        pings = sorted(server_ping, key=server_ping.get)
        res = {'pings': [pings[0], pings[1]]}
        return JsonResponse(res)
