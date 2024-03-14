from django import forms
from .models import ContactsModal

class ContactsForms(forms.ModelForm):
	class Meta:
		model = ContactsModal
		fields = '__all__'
