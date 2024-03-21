from django.views import View
from django.views.generic import CreateView
from .models import ContactInfo, hiroBlock, footerInfo
from .forms import ContactsForms
from django.shortcuts import render


class ContactPage(View):
	def get(self, request):
		contacts = ContactInfo.objects.all()
		form = ContactsForms
		return render(request, 'main/contact.html', {"contacts": contacts, "form": form})


class CreateContact(CreateView):
	form_class = ContactsForms
	success_url = '/contacts/'

	def get_template_names(self):
		return ['main/contact.html']


