from django.urls import path
from . import views

urlpatterns = [
    path('', views.WorksListView.as_view(), name='works_list'),
    path('<slug:slug>/', views.WorksDetailView.as_view(), name='work_detail'),
]
