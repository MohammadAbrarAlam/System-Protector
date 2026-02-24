from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render,redirect

from .monitoring import get_system_status, get_process_list
from .firewall import firewall_status
from .encryption import encrypt_data
from .models import Patch
from .serializers import PatchSerializer




# =========================
# REST API VIEWS
# =========================

@api_view(['GET'])
def system_status(request):
    data = get_system_status()
    return Response(data)


@api_view(['GET'])
def processes(request):
    data = get_process_list()
    return Response(data)


@api_view(['GET'])
def firewall(request):
    data = firewall_status()
    return Response({"firewall": data})


@api_view(['POST'])
def encrypt(request):
    text = request.data.get("text")
    encrypted = encrypt_data(text)
    return Response({"encrypted": encrypted})


@api_view(['GET'])
def patches(request):
    patch = Patch.objects.all()
    serializer = PatchSerializer(patch, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def add_patch(request):
    serializer = PatchSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


# =========================
# TEMPLATE (HTML) VIEWS
# =========================

# Dashboard page
def dashboard(request):
    return render(request, "dashboard.html")


# System status HTML page
def system_status_page(request):
    data = get_system_status()
    return render(request, "system_status.html", data)


# Processes HTML page
def processes_page(request):
    data = get_process_list()
    return render(request, "processes.html", {"processes": data})


# Firewall HTML page
def firewall_page(request):
    data = firewall_status()
    return render(request, "firewall.html", {"firewall": data})


'''
Patch management HTML page
def patches_page(request):
    data = Patch.objects.all()
    return render(request, "patches.html", {"patches": data})
'''

# Patches 
def patches_page(request):
  if request.method == "POST":
    system_name = request.POST.get("system_name")
    patch_version = request.POST.get("patch_version")
    status = request.POST.get("status")
    Patch.objects.create(
            system_name=system_name,
            patch_version=patch_version,
            status=status
    )
    return redirect("patches")

  patches = Patch.objects.all().order_by('-date')
  return render(request,
                  "patches.html",
                  {"patches": patches})