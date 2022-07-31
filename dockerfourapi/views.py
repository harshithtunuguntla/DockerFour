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
    try:    
    
        res=sp.run(["systemctl", "start","docker"],capture_output=True)
        print(res.returncode)
        # res=subprocess.run(["dockerd"],capture_output=True)
        res=sp.run(["docker","info"],capture_output=True)
        print("FINAL")
        #print(res)

    except Exception as e:
        print("IN EXCEPTION INSTALLING")
        res =  sp.run(["apt-get", "install", "docker.io", "-y"], capture_output=True)
        # print("Waiting to install")
        # time.sleep(10)
        # print("DONe")
        res=sp.run(["systemctl", "start","docker"],capture_output=True)
        print(res.returncode)

    return HttpResponse("Docker Installed Succesfully")

def dockeruninstall_view(request):
    try:
        res=sp.run(["apt", "remove","docker.io","-y"],capture_output=True)
    except:
        pass

    try:
        sp.run(["rm","-r","/var/run/docker"],capture_output=True)
    except:
        pass


    try:
        sp.run(["rm","/var/run/docker.sock"],capture_output=True)
    except:
        pass

    try:
        sp.run(["rm","/var/run/docker.pid"],capture_output=True)
    except:
        pass
    try:
        sp.run(["rm","-r","/var/lib/docker"],capture_output=True)
    except:
        pass
    return HttpResponse("Docker Uninstall Succesfully")
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


#-------------------------------- Image Pull and Delete
def pullimage_view(request,image_name):
    print("IMAGES")
    print("Inside images pull  view")
    try:
        res=sp.run(["docker","pull",image_name],capture_output=True)
        return HttpResponse(res.stdout.decode())
        # return HttpResponse("Inside images info view")

    except Exception as e:
        return HttpResponse(e)

def deleteimage_view(request,image_name):
    try:
        res=sp.run(["docker","rmi","-f",image_name],capture_output=True)
        return HttpResponse(res.stdout.decode())
    except Exception as e:
        return HttpResponse(e)

#-------------------------------

def deletecontainer_view(request,container_id):
    try:
        res=sp.run(["docker","rm","-f",container_id],capture_output=True)
        if res.stdout.decode()==container_id:
            return HttpResponse("Container Deleted Succesfully")
        elif res.stdout.decode()=="":
            return HttpResponse("Container Could Not Be Found")
        else:
            return HttpResponse("There is a problem executing command")
    except Exception as e:
        return HttpResponse(e)

def stopcontainer_view(request,container_id):
    try:
        res=sp.run(["docker","stop",container_id],capture_output=True)
        return HttpResponse(res.stdout.decode())
    except Exception as e:
        return HttpResponse(e)

def pausecontainer_view(request,container_id):
    try:
        res=sp.run(["docker","pause",container_id],capture_output=True)
        return HttpResponse(res.stdout.decode())
    except Exception as e:
        return HttpResponse(e)



