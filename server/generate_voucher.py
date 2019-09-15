from server.models import *
import random
from django.db import IntegrityError
import pysnooper


def add_voucher(rnd, profile, profile_id, reseller, reseller_id):
    Voucher(name=f'Arex{rnd}', batch='', status='new', user_id='189', created='2019-08-27 16:22:24',
             modified='2019-08-27 20:00:01', extra_name='', extra_value='', password=rnd + 1, realm=reseller,
             realm_id=reseller_id, profile=profile, profile_id=profile_id, expire='', time_valid='30-00-00-0',
             time_used='0', time_cap='2592000').save()
    add_radchack(rnd, profile, profile_id)


def add_radchack(rnd, profile, reseller):
    Radcheck(username=f'Arex{rnd}', attribute='User-Profile', op=':=', value=profile).save()
    Radcheck(username=f'Arex{rnd}', attribute='Rd-Realm', op=':=', value=reseller).save()
    Radcheck(username=f'Arex{rnd}', attribute='Cleartext-Password', op=':=', value=rnd + 1).save()
    Radcheck(username=f'Arex{rnd}', attribute='Rd-Voucher', op=':=', value='30-00-00-00').save()
    Radcheck(username=f'Arex{rnd}', attribute='Rd-User-Type', op=':=', value='voucher').save()


def run(profile, profile_id, reseller, reseller_id, item, count):
    item.status = 'Running'
    item.save()
    for i in range(count):
        try:
            rnd = random.randint(1000000000, 9999999999)
            add_voucher(rnd, profile, profile_id, reseller, reseller_id)
        except IntegrityError:
            run(profile, profile_id, reseller, reseller_id)
    item.status = 'Done'
    item.save()
