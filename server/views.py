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
            print(voucher.profile.name)
            regex = re.search(r'(.+)mb-(\d)m', voucher.profile.name)
            max_data = int(regex[1]) * 1000000  # MegaByte to Byte
            max_time = int(regex[2]) * 30 * 24 * 60 * 60  # Month to Second
            data = max_data - voucher.data_used
            time = max_time - voucher.time_used
        except Exception:
            return JsonResponse({'message': 'ok'}, status=401)
        res = {'data': data, 'time': time}
        return JsonResponse(res)


class Ping(View):
    def get(self, request):
        return JsonResponse({'message': 'pong'})
