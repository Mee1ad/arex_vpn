from django.db import models
from django.forms import ModelForm


class Countrie(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    iso_code = models.CharField(max_length=2, blank=True, null=True)
    icon_file = models.CharField(max_length=100, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'countries'


class Group(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'groups'


class Language(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    iso_code = models.CharField(max_length=2, blank=True, null=True)
    rtl = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'languages'


class User(models.Model):
    def __str__(self):
        return self.username

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
    country = models.ForeignKey(Countrie, on_delete=models.PROTECT, blank=True, null=True)
    group = models.ForeignKey(Group, on_delete=models.PROTECT)
    language = models.ForeignKey(Language, on_delete=models.PROTECT, blank=True, null=True)
    parent = models.ForeignKey('self', on_delete=models.PROTECT, blank=True, null=True)
    lft = models.IntegerField(blank=True, null=True)
    rght = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'users'


class Realm(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=64)
    available_to_siblings = models.IntegerField()
    icon_file_name = models.CharField(max_length=128)
    phone = models.CharField(max_length=14, blank=True, null=True)
    fax = models.CharField(max_length=14, blank=True, null=True)
    cell = models.CharField(max_length=14, blank=True, null=True)
    email = models.CharField(max_length=128, blank=True, null=True)
    url = models.CharField(max_length=128, blank=True, null=True)
    street_no = models.CharField(max_length=10, blank=True, null=True)
    street = models.CharField(max_length=50, blank=True, null=True)
    town_suburb = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    twitter = models.CharField(max_length=255, blank=True, null=True)
    facebook = models.CharField(max_length=255, blank=True, null=True)
    youtube = models.CharField(max_length=255, blank=True, null=True)
    google_plus = models.CharField(max_length=255, blank=True, null=True)
    linkedin = models.CharField(max_length=255, blank=True, null=True)
    t_c_title = models.CharField(max_length=255, blank=True, null=True)
    t_c_content = models.TextField(blank=True, null=True)
    suffix = models.CharField(max_length=200, blank=True, null=True)
    suffix_permanent_users = models.IntegerField()
    suffix_vouchers = models.IntegerField()
    suffix_devices = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'realms'


class Profile(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=128)
    available_to_siblings = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'profiles'


class ProfileComponent(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=128)
    available_to_siblings = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.PROTECT,
                             blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'profile_components'


class Voucher(models.Model):
    name = models.CharField(unique=True, max_length=64, blank=True, null=True)
    batch = models.CharField(max_length=128, blank=True, null=True)
    status = models.CharField(max_length=8, blank=True, null=True)
    perc_time_used = models.IntegerField(blank=True, null=True)
    perc_data_used = models.IntegerField(blank=True, null=True)
    last_accept_time = models.DateTimeField(blank=True, null=True)
    last_reject_time = models.DateTimeField(blank=True, null=True)
    last_accept_nas = models.CharField(max_length=128, blank=True, null=True)
    last_reject_nas = models.CharField(max_length=128, blank=True, null=True)
    last_reject_message = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    extra_name = models.CharField(max_length=100, blank=True, null=True)
    extra_value = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=30)
    realm = models.CharField(max_length=50)
    realm = models.ForeignKey(Realm, on_delete=models.PROTECT, blank=True, null=True)
    profile = models.CharField(max_length=50)
    profile = models.ForeignKey(Profile, on_delete=models.PROTECT, blank=True, null=True)
    expire = models.CharField(max_length=10, blank=True, null=True)
    time_valid = models.CharField(max_length=10)
    data_used = models.BigIntegerField(blank=True, null=True)
    data_cap = models.BigIntegerField(blank=True, null=True)
    time_used = models.IntegerField(blank=True, null=True)
    time_cap = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vouchers'


class UserGenerator(models.Model):
    count = models.IntegerField(default=1)
    realm = models.ForeignKey(Realm, on_delete=models.SET_NULL, blank=True, null=True)
    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, blank=True, null=True)
    status = models.CharField(max_length=255, default='New')
    error = models.TextField(null=True, blank=True, verbose_name='error')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user_generator'


class Radcheck(models.Model):
    username = models.CharField(max_length=64)
    attribute = models.CharField(max_length=64, choices=[(1, 'Rd-Reset-Type-Data'), (2, 'Rd-Cap-Type-Data'),
                                                         (3, 'Rd-Total-Data'), (4, 'Rd-Reset-Type-Time'),
                                                         (5, 'Rd-Cap-Type-Time'), (6, 'Rd-Total-Time')])
    op = models.CharField(max_length=2)
    value = models.CharField(max_length=253)

    class Meta:
        managed = False
        db_table = 'radcheck'


class ApiUser(models.Model):
    pin = models.CharField(max_length=31)
    device_id = models.CharField(max_length=127, unique=True)
    device = models.CharField(max_length=127)
    os = models.CharField(max_length=127)
    ip = models.CharField(max_length=31)
    mac = models.CharField(max_length=127)

    class Meta:
        db_table = 'api_user'


class ApiHit(models.Model):
    url = models.URLField()

    class Meta:
        db_table = 'api_hit_address'


class ProfileComponentForm(ModelForm):

    class Meta:
        model = ProfileComponent
        fields = ['name', 'available_to_siblings', 'user']