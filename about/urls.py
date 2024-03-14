from django.urls import path
from . import views

urlpatterns = [
	path('contacts/', views.ContactPage.as_view(), name="contacts"),
	path('feedback/', views.CreateContact.as_view(), name="faatbicke"),
]
