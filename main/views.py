from django.shortcuts import render
from news.models import reviews

def index(request):
    all_reviews = reviews.objects.all()  # Получите все отзывы из базы данных
    return render(request, 'main/home.html', {'all_reviews': all_reviews})


def about(request):
	return render(request, 'main/about.html')