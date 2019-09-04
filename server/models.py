# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Countries(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    iso_code = models.CharField(max_length=2, blank=True, null=True)
    icon_file = models.CharField(max_length=100, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'countries'


class Groups(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'groups'


class Languages(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    iso_code = models.CharField(max_length=2, blank=True, null=True)
    rtl = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'languages'


class Users(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=50)
    token = models.CharField(max_length=36, blank=True, null=True)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    active = models.IntegerField()
    monitor = models.IntegerField()
    country = models.ForeignKey(Countries, on_delete=models.PROTECT, blank=True, null=True)
    group = models.ForeignKey(Groups, on_delete=models.PROTECT)
    language = models.ForeignKey(Languages, on_delete=models.PROTECT, blank=True, null=True)
    parent = models.ForeignKey('self', on_delete=models.PROTECT, blank=True, null=True)
    lft = models.IntegerField(blank=True, null=True)
    rght = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'users'


class Realms(models.Model):
    name = models.CharField(max_length=64)
    available_to_siblings = models.IntegerField()
    icon_file_name = models.CharField(max_length=128)
    phone = models.CharField(max_length=14)
    fax = models.CharField(max_length=14)
    cell = models.CharField(max_length=14)
    email = models.CharField(max_length=128)
    url = models.CharField(max_length=128)
    street_no = models.CharField(max_length=10)
    street = models.CharField(max_length=50)
    town_suburb = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    lat = models.FloatField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)
    user = models.ForeignKey(Users, on_delete=models.PROTECT, blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    twitter = models.CharField(max_length=255)
    facebook = models.CharField(max_length=255)
    youtube = models.CharField(max_length=255)
    google_plus = models.CharField(max_length=255)
    linkedin = models.CharField(max_length=255)
    t_c_title = models.CharField(max_length=255)
    t_c_content = models.TextField()
    suffix = models.CharField(max_length=200)
    suffix_permanent_users = models.IntegerField()
    suffix_vouchers = models.IntegerField()
    suffix_devices = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'realms'


class Profiles(models.Model):
    name = models.CharField(max_length=128)
    available_to_siblings = models.IntegerField()
    user = models.ForeignKey(Users, on_delete=models.PROTECT, blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'profiles'


class Vouchers(models.Model):
    name = models.CharField(unique=True, max_length=64, blank=True, null=True)
    batch = models.CharField(max_length=128)
    status = models.CharField(max_length=8, blank=True, null=True)
    perc_time_used = models.IntegerField(blank=True, null=True)
    perc_data_used = models.IntegerField(blank=True, null=True)
    last_accept_time = models.DateTimeField(blank=True, null=True)
    last_reject_time = models.DateTimeField(blank=True, null=True)
    last_accept_nas = models.CharField(max_length=128, blank=True, null=True)
    last_reject_nas = models.CharField(max_length=128, blank=True, null=True)
    last_reject_message = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey(Users, on_delete=models.PROTECT, blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    extra_name = models.CharField(max_length=100)
    extra_value = models.CharField(max_length=100)
    password = models.CharField(max_length=30)
    realm = models.CharField(max_length=50)
    realm = models.ForeignKey(Realms, on_delete=models.PROTECT, blank=True, null=True)
    profile = models.CharField(max_length=50)
    profile = models.ForeignKey(Profiles, on_delete=models.PROTECT, blank=True, null=True)
    expire = models.CharField(max_length=10)
    time_valid = models.CharField(max_length=10)
    data_used = models.BigIntegerField(blank=True, null=True)
    data_cap = models.BigIntegerField(blank=True, null=True)
    time_used = models.IntegerField(blank=True, null=True)
    time_cap = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vouchers'


class ApiUser(models.Model):
    device_id = models.CharField(max_length=255)

