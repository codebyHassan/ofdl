from django.urls import path
from app import views

urlpatterns = [
    path('', views.home, name='home'  ),
    path('services', views.demo , name='demo'), 
    path('track/', views.track_shipment, name='track_shipment'),
]
