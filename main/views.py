from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse, Http404
from django.contrib import auth
from . import interfaces_api
import json
# Create your views here.


def index(request):
    if request.user.is_authenticated:
        context = {"interfaces": interfaces_api.get_interfaces()}
        return render(request, 'index.html', context)
    else:
        err = request.GET.get("error")
        context = {"err":err}
        return render(request, 'auth.html', context)

def login(request):
    if request.method != 'POST':
        raise Http404
    else:
        data = request.POST
        login = data.get("login")
        password = data.get("password")
        print(login, password)
        user = auth.authenticate(request, username=login, password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect("/")
        else:
            return HttpResponseRedirect("/?error=login")

def ajax(request):
    if request.method != 'POST':
        raise Http404
    else:
        data = json.loads(request.POST.get("data"))
        return JsonResponse(interfaces_api.change_ips(data))