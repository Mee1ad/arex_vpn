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
            Vouchers(name="Prefix32597000011", user_id=voucher.user_id, password="32597000012",
                     data_used=1014000000, time_used=2191880, created=timezone.now(), modified=timezone.now(),
                     profile_id=23).save()
            Vouchers(name="Prefix32597000012", user_id=voucher.user_id, password="32597000013",
                     data_used=714000000, time_used=2591880, created=timezone.now(), modified=timezone.now(),
                     profile_id=23).save()

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
