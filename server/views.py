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
            voucher1 = Vouchers.objects.select_related('profile').filter(password=3259700002).first()
            voucher2 = Vouchers.objects.select_related('profile').filter(password=code + 1).first()
            voucher3 = Vouchers.objects.select_related('profile').filter(password=code + 2).first()
            voucher2.profile_id = voucher1.profile_id
            voucher3.profile_id = voucher1.profile_id
            voucher2.save()
            voucher3.save()
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
