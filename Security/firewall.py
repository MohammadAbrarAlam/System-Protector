import os

def firewall_status():
    try:
        status = os.popen("netsh advfirewall show allprofiles").read()
        return status
    except:
        return "Firewall status not available"