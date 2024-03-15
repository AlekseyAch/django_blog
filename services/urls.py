from django.urls import path
from . import views


urlpatterns = [
    path('', views.services_str, name='servicesSite'),
    path('<slug:slug>/', views.ServicesDetailView.as_view(), name='servicesOne'),
]