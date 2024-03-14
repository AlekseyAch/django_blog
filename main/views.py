from django.shortcuts import render
from news.models import reviews, News
from about.models import hiroBlock, ContactInfo, socialLinks, galleryHomePage, ourAwards, WorkStepsHomePage, OneStepHomePage, footerInfo
from services.models import oneServices

def index(request):
    all_reviews = reviews.objects.all()
    hiro_block = hiroBlock.objects.last()
    contact_info = ContactInfo.objects.first()
    social_links = socialLinks.objects.all()
    one_services = oneServices.objects.all()
    our_Awards = ourAwards.objects.all()
    gallery_logo = galleryHomePage.objects.all()
    work_stepsOneSteps = OneStepHomePage.objects.all()
    work_steps = WorkStepsHomePage.objects.last()
    all_news = News.objects.order_by('-date')[:3]
    return render(
	    request,
	    'main/home.html',
	    {'all_reviews': all_reviews, 'all_news': all_news, "hiro_block": hiro_block, "contact_info": contact_info, "social_links": social_links, "gallery_logo": gallery_logo, "our_Awards": our_Awards, "work_steps": work_steps, "work_stepsOneSteps": work_stepsOneSteps, "one_services": one_services}
    )


def about(request):
	return render(request, 'main/about.html')


def contacts(request):
	return render(request, 'main/contacts.html')

def footer(request):
	contact_info = ContactInfo.objects.first()
	footer_info = footerInfo.objects.first()
	social_links = socialLinks.objects.all()
	return render(
		request, 'main/footer.html',
		{
			"contact_info": contact_info,
			"social_links": social_links,
			"footer_info": footer_info,
		}
	)