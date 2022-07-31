from django.shortcuts import render
from django.http import HttpResponse
import subprocess as sp

# Create your views here.

#Is docker installed
def dockerinstallation_view(request):
    return HttpResponse("Inside docker installation view, is docker installed")

#---------------------
#Install Docker
def dockerinstall_view(request):
    return HttpResponse("Inside docker install view")

def dockeruninstall_view(request):
    return HttpResponse("Inside docker uninstall view")
#----------------------

#Processes

def allprocesses_view(request):
    print("All Processes")
    print("Inside Inside all processes view")
    try:
        res=sp.run(["docker","ps","-a"],capture_output=True)
        return HttpResponse(res.stdout.decode())
        # return HttpResponse("Inside images info view")

    except Exception as e:
        return HttpResponse(e)


def pausedprocesses_view(request):
    print("Paused Processes")
    print("Inside Paused all processes view")
    try:
        res=sp.run(["docker","ps","--filter","status=paused"],capture_output=True)
        return HttpResponse(res.stdout.decode())
        # return HttpResponse("Inside images info view")

    except Exception as e:
        return HttpResponse(e)


def currentprocesses_view(request):
    print("Current Processes")
    print("Inside current all processes view")
    try:
        res=sp.run(["docker","ps"],capture_output=True)
        return HttpResponse(res.stdout.decode())
        # return HttpResponse("Inside images info view")

    except Exception as e:
        return HttpResponse(e)

def allprocesseswithsize_view(request):
    print("All Processes with size")
    print("Inside all processes with size view")
    try:
        res=sp.run(["docker","ps","-a","-s"],capture_output=True)
        return HttpResponse(res.stdout.decode())
        # return HttpResponse("Inside images info view")

    except Exception as e:
        return HttpResponse(e)

#------------------------

#Info

def allinfo_view(request):
    print("Info")
    print("Inside info view")
    try:
        res=sp.run(["docker","info"],capture_output=True)
        return HttpResponse(res.stdout.decode())
        # return HttpResponse("Inside images info view")

    except Exception as e:
        return HttpResponse(e)

def imagesinfo_view(request):
    print("IMAGES")
    print("Inside images info view")
    try:
        res=sp.run(["docker","images"],capture_output=True)
        return HttpResponse(res.stdout.decode())
        # return HttpResponse("Inside images info view")

    except Exception as e:
        return HttpResponse(e)

