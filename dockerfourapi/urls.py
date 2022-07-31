
from os import name
from django.urls import path

from . import views


urlpatterns = [

    
    path('docker/is_installed',views.dockerinstallation_view,name="install_docker"),


    path('docker/install',views.dockerinstall_view,name="install_docker"),
    path('docker/uninstall',views.dockeruninstall_view,name="uninstall_docker"),


    path('processes/list/all',views.allprocesses_view,name="all_processes"),
    path('processes/list/paused',views.pausedprocesses_view,name="paused_processes"),
    path('processes/list/current',views.currentprocesses_view,name="current_processes"),
    path('processes/list/all_s',views.allprocesseswithsize_view,name="all_processes_s"),

    path('info/all',views.allinfo_view,name="all_info"),
    path('info/images',views.imagesinfo_view,name="images_info"),





    ]