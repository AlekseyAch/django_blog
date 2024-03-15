from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.http import Http404
from django.shortcuts import redirect
from django.views.generic.base import View
from django.views.generic import DetailView
from .models import oneServices, accardionServices
from about.models import WorkStepsHomePage, OneStepHomePage, ContactInfo
from django.shortcuts import render

def services_str(request):
    one_services = oneServices.objects.all()
    work_steps = WorkStepsHomePage.objects.last()
    work_stepsOneSteps = OneStepHomePage.objects.all()
    contact_info = ContactInfo.objects.first()
    return render(request, 'services/services.html', {
        "one_services": one_services,
        "work_steps": work_steps,
        "work_stepsOneSteps": work_stepsOneSteps,
        "contact_info": contact_info
    })


class ServicesDetailView(DetailView):
    model = oneServices
    template_name = 'services/serviceDetails.html'
    context_object_name = 'services_post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services_perent'] = self.object  # передаем объект News в контекст
        context['services_one'] = oneServices.objects.all()
        context['accardion_services'] = accardionServices.objects.all()
        return context
