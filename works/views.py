from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import works, WorksCategory, WorksGallery
from django.shortcuts import get_object_or_404
from about.models import WorkStepsHomePage, OneStepHomePage, socialLinks

class WorksListView(ListView):
    model = works
    context_object_name = 'works_list'
    works_category = WorksCategory.objects.all()
    work_steps = WorkStepsHomePage.objects.last()
    work_stepsOneSteps = OneStepHomePage.objects.all()
    template_name = 'works/protfolio.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['works_category'] = WorksCategory.objects.all()
        context['work_steps'] = WorkStepsHomePage.objects.last()
        context['work_stepsOneSteps'] = OneStepHomePage.objects.all()
        return context

class WorksDetailView(DetailView):
    model = works
    template_name = 'works/protfolioDetails.html'
    context_object_name = 'work'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        gallery = self.get_object()
        context['social_links'] = socialLinks.objects.all()
        context['work_gallary'] = WorksGallery.objects.filter(gallery=gallery)
        context['works_list'] = works.objects.all().order_by('-id')[:2]
        return context