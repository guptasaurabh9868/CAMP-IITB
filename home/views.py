from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
import ldap
from django_auth_ldap.config import LDAPSearch
from django.conf import settings
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django_auth_ldap.backend import _LDAPUser, LDAPBackend
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
import datetime
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from ldap3 import (HASHED_SALTED_SHA, MODIFY_REPLACE)
from ldap3.utils.hashed import hashed
# from django.core.mixins import SensitivePostParametersMixin

# from .forms import LoginForm

# Create your views here.

# class LoginView(View):
#     """
#     GET: If user is already logged in then redirect to 'next' parameter in query_params
#         Else render the login form
#     POST:
#         Validate form, login user
#     """
#     form_class = LoginForm
#     template_name = 'home/main.html'


def home(request):
    login_failed = False
    authorized_Access = True
    if request.POST:
        usern = request.POST.get("username", '')
        passw = request.POST.get("password", '')

        user = authenticate(username=usern, password=passw)
        if user is not None:
            login(request, user)
            return redirect('/userinfo/')
        else:
            login_failed = True
    return render(request, 'home/main.html', {'login_failed': login_failed,'authorized_Access':authorized_Access})


def userinfo(request):
    if request.POST:
        logout(request)
        return HttpResponseRedirect('/')
    else:
        print(request.user.email)

        if request.user.is_authenticated:
            start_date = "01-01-1970"
            date_1 = datetime.datetime.strptime(start_date, "%m-%d-%Y")
            # print(type(request.user.userprofile.shadowexpire))
            shadowexpire = int('0'+request.user.userprofile.shadowexpire.strip())
            print(type(shadowexpire))
            end_date = date_1 + datetime.timedelta(days=int(shadowexpire))
            return render(request, 'home/userinfo.html',{'shadowexpire':end_date})
        else:
            return render(request, 'home/userinfo.html')


# @login_required
# def userinfo(request):
#     try:
#         ldapuserprofile = UserProfile.objects.get(username=request.user.username)
#     except UserProfile.DoesNotExist:
#         return HttpResponseRedirect('/logout/')
#     context = {'request': request, 'ldapuser': ldapuserprofile,}
#     return render(request, 'home/userinfo.html', context)

def depart_sysad(request):
    return render(request,'home/depart_sysad.html')
def changeuid(request):
    return render(request,'home/changeuid.html')
def hostel_sysad(request):
    return render(request,'home/hostel_sysad.html')
def passwordchange(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            # user = form.save()
            # update_session_auth_hash(request, user)  # Important!
            dn = request.user.entry_get_dn()
            hashed_password = hashed(HASHED_SALTED_SHA, request.user.password)
            changes = {'userPassword': [(MODIFY_REPLACE, [hashed_password])]}
            success = self.connection.modify(dn, changes=changes)
            if not success:
                print('Unable to change password for %s' % dn)
                print(self.connection.result)
                raise ValueError('Unable to change password')
            messages.success(request, 'Your password was successfully updated!')
            # os command
            return redirect('passwordchange')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'home/passwordchange.html', {'form': form})
def modify_details(request):
    return render(request,'home/modify-details.html')
def setup_auto(request):
    return render(request,'home/setup_auto.html')
def web_quota(request):
    return render(request,'home/web_quota.html')