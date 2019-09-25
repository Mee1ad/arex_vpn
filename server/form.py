from django import forms
from server.models import *


class ProfileForm(forms.Form):
    # profile component time
    pct_name = forms.CharField(label='name', max_length=100)
    pct_available_to_siblings = forms.BooleanField(label='available to siblings')
    pct_user = forms.IntegerField(label='user')
    # profile component data
    pcd_name = forms.CharField(label='name', max_length=100)
    pcd_available_to_siblings = forms.BooleanField(label='available to siblings')
    pcd_user = forms.IntegerField(label='user')
    # profile
    p_name = forms.CharField(label='name', max_length=100)
    p_available_to_siblings = forms.BooleanField(label='available to siblings')
    p_user = forms.IntegerField(label='user')
    # radgroupcheck data
    d_groupname1 = forms.CharField(label='groupname', max_length=100)
    d_attribute1 = forms.CharField(label='attribute', max_length=100)
    d_op1 = forms.CharField(label='op', max_length=100)
    d_value1 = forms.CharField(label='value', max_length=100)
    # d_comment1 = forms.CharField(label='comment', max_length=100)
    # radgroupcheck data 2
    d_groupname2 = forms.CharField(label='groupname', max_length=100)
    d_attribute2 = forms.CharField(label='attribute', max_length=100)
    d_op2 = forms.CharField(label='user', max_length=100)
    d_value2 = forms.CharField(label='user', max_length=100)
    # d_comment2 = forms.CharField(label='user', max_length=100)
    # radgroupcheck data 3
    d_groupname3 = forms.CharField(label='groupname', max_length=100)
    d_attribute3 = forms.CharField(label='attribute', max_length=100)
    d_op3 = forms.CharField(label='user', max_length=100)
    d_value3 = forms.CharField(label='user', max_length=100)
    # d_comment3 = forms.CharField(label='user', max_length=100)
    # radgroupcheck time
    t_groupname1 = forms.CharField(label='groupname', max_length=100)
    t_attribute1 = forms.CharField(label='attribute', max_length=100)
    t_op1 = forms.CharField(label='user', max_length=100)
    t_value1 = forms.CharField(label='user', max_length=100)
    # t_comment1 = forms.CharField(label='user', max_length=100)
    # radgroupcheck time 2
    t_groupname2 = forms.CharField(label='groupname', max_length=100)
    t_attribute2 = forms.CharField(label='available to siblings', max_length=100)
    t_op2 = forms.CharField(label='user', max_length=100)
    t_value2 = forms.CharField(label='user', max_length=100)
    # t_comment2 = forms.CharField(label='user', max_length=100)
    # radgroupcheck time 3
    t_groupname3 = forms.CharField(label='name', max_length=100)
    t_attribute3 = forms.CharField(label='available to siblings', max_length=100)
    t_op3 = forms.CharField(label='user', max_length=100)
    t_value3 = forms.CharField(label='user', max_length=100)
    # t_comment3 = forms.CharField(label='user', max_length=100)
    # radusergroup
    rdg_username = forms.CharField(max_length=100)
    rdg_groupname = forms.CharField(label='groupname', max_length=100)
    rdg_priority = forms.IntegerField(label='priority')
    # radusergroup 2
    rdg_username2 = forms.CharField(label='username2', max_length=100)
    rdg_groupname2 = forms.CharField(label='groupname2', max_length=100)
    rdg_priority2 = forms.IntegerField(label='priority')

