from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http.response import HttpResponseBadRequest
from django.contrib.auth.decorators import login_required
from .models import Tenant
from django.contrib.auth.models import User

# Create your views here.
@login_required
def my_home(request):
    tenancies = request.user.tenants.all()
    print(tenancies)
    url_tenant = request.get_host().split('.')[0]
    if request.user.username == url_tenant:
        # print(request.COOKIES)
        # print(request.get_host())
        return HttpResponse("<h1>Test view</h1>")
    else:
        return HttpResponseBadRequest('<h1>You are not allowed to see this.</h1>')