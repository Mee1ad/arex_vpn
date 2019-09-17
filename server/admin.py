from django.contrib import admin
from server.models import *
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.utils.html import escape
from server import generate_voucher
# Register your models here.


def get_user(obj):
    if obj.user:
        print(obj.user)
        link = reverse("admin:auth_user_change", args=[obj.user.id])
        return mark_safe(f'<a href="{link}">{escape(obj.user)}</a>')
    return ''


class VoucherAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'link_to_user', 'perc_time_used', 'perc_data_used', 'realm')
    list_filter = ('status', 'realm', 'status')
    list_display_links = ('name',)
    search_fields = ['name']
    list_per_page = 10
    ordering = ('-created',)

    def link_to_user(self, obj):
        return get_user(obj)

    link_to_user.short_description = 'User'


class RadgroupcheckAdmin(admin.ModelAdmin):
    list_display = ('groupname', 'attribute', 'op', 'value', 'comment')
    search_fields = ['groupname']
    list_per_page = 10
    ordering = ('-id',)


class RealmAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'link_to_user', 'city')
    list_filter = ('name', 'city', 'email')
    search_fields = ['name', 'email', 'city']
    list_per_page = 10
    ordering = ('-created',)

    def link_to_user(self, obj):
        return get_user(obj)

    link_to_user.short_description = 'User'


class UserGeneratorAdmin(admin.ModelAdmin):
    list_display = ('edit', 'count', 'realm', 'profile', 'status', 'error')
    list_display_links = ('edit', 'error')
    search_fields = ['count', 'realm', 'profile', 'status']
    actions = ["generate_queries"]

    def generate_queries(self, request, queryset):
        for item in queryset:
            generate_voucher.run(item.profile, item.profile_id, item.realm, item.realm_id,
                                 item, item.count)

    def edit(self, obj):
        return 'Edit'

    generate_queries.short_description = 'Generate selected queries'


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'available_to_siblings', 'link_to_user',)
    list_filter = ('name',)
    search_fields = ['name', 'user']
    list_per_page = 10
    ordering = ('-created',)

    def link_to_user(self, obj):
        return get_user(obj)

    link_to_user.short_description = 'User'


class ProfileComponentAdmin(admin.ModelAdmin):
    list_display = ('name', 'available_to_siblings', 'link_to_user')
    list_filter = ('name', )
    search_fields = ['name', 'user']
    list_per_page = 10
    ordering = ('-created',)

    def link_to_user(self, obj):
        return get_user(obj)

    link_to_user.short_description = 'User'


admin.site.register(Voucher, VoucherAdmin)
admin.site.register(Realm, RealmAdmin)
admin.site.register(UserGenerator, UserGeneratorAdmin)
admin.site.register(Radgroupcheck, RadgroupcheckAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(ProfileComponent, ProfileComponentAdmin)
