from django.shortcuts import render
from .models import Shipment
# Create your views here.
def home(request):
    return render(request, 'home.html')


def demo(request):
    """
    Demo page for all spare navigation links
    """
    context = {
        'page_title': 'Services - Demo Page',
    }
    return render(request, 'demo.html', context)

from .models import Shipment

def track_shipment(request):
    """
    View to track shipment by tracking ID
    """
    tracking_id = request.GET.get("tracking_id", "").strip().upper()
    shipment = None
    
    if tracking_id:
        shipment = Shipment.objects.filter(tracking_id=tracking_id).first()
    
    context = {
        "shipment": shipment,
    }
    
    return render(request, "fuck.html", context)