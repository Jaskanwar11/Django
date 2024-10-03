from django.shortcuts import render
from .models import AppVariety
from django.shortcuts import get_object_or_404

# Create your views here.
def app(request):
    apps = AppVariety.objects.all()
    return render(request, 'App/app.html', {'apps' : apps})

def app_details(request, app_id):
    app = get_object_or_404(AppVariety, pk = app_id)
    return render(request, 'App/app_details.html', {'app': app})

def app_pricing(request, app_id):
    price = get_object_or_404(AppVariety, pk = app_id)
    return render(request, 'App/app_pricing.html', {'price': price})

def app_store_view(request):
    return render(request, 'App/app_stores.html')