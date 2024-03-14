from django.urls import path
from . import views
from .views import search_view


urlpatterns = [
    path('', views.news_str, name='services'),

]