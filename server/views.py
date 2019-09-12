from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse
from server.models import *
import json
import re
import jwt
import pysnooper
from django.utils import timezone


class Login(View):
    @pysnooper.snoop()
    def post(self, request):
        data = json.loads(request.body)
        code = int(data['code'])
        # device_id = data['device_id']
        voucher = Vouchers.objects.select_related('profile').filter(password=code + 1).first()
        if voucher is None:
            return JsonResponse({'message': 'ok'}, status=404)
        voucher.profile.name = voucher.profile.name.lower()
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
        return JsonResponse({'message': 'pong'})
