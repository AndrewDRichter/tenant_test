from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def my_home(request):
    print("-------view init------")
    # print(request.META)
    print("-------view end------")
    # print(request.COOKIES)
    print(request.get_host())
    return HttpResponse("<h1>Test view</h1>")