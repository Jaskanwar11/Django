from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.app, name = 'App'),
    path('<int:app_id>/', views.app_details, name = 'app_details'),
    path('<int:app_id>/', views.app_pricing, name = 'app_pricing'),
    path('app_stores/', views.app_store_view, name = 'app_stores'),

]