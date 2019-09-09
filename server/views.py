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
        try:
            voucher = Vouchers.objects.select_related('profile').filter(password=code + 1).first()
            voucher.profile.name = voucher.profile.name.lower()
            print(voucher.profile.name)
            data = voucher.data_cap - voucher.data_used
            time = voucher.time_used
            print('time_used:', voucher.time_used)
            print('data_used:', voucher.data_used)
        except Exception:
            return JsonResponse({'message': 'ok'}, status=401)
        res = {'data': data, 'data_cap': voucher.data_cap, 'time': time, 'time_cap': voucher.time_cap}
        return JsonResponse(res)


class Ping(View):
    def get(self, request):
        return JsonResponse({'message': 'pong'})
