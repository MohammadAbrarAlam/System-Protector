from django.urls import path
from . import views

urlpatterns = [

    # Template URLs
    path('', views.dashboard, name="dashboard"),
    path('system-status/', views.system_status_page),
    path('processes/', views.processes_page),
    path('firewall/', views.firewall_page),
    #path('patches/', views.patches_page),
    path('patches/', views.patches_page, name="patches"),

    # REST API URLs
    path('api/system-status/', views.system_status),
    path('api/processes/', views.processes),
    path('api/firewall/', views.firewall),
    path('api/encrypt/', views.encrypt),
    path('api/patches/', views.patches),
    path('api/add-patch/', views.add_patch),
]