from django.shortcuts import render, HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse
from django.views.generic import DetailView
from django.http import Http404
from django.shortcuts import redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from .import_from_wordpress import import_wordpress_data
from .models import News, Tag, Category, reviews, Response
from django.views.generic.base import View
from django.shortcuts import get_object_or_404
from .forms import ReviewsForm, ResponseForm

def news_str(request):
    current_date = timezone.now()
    news_list = News.objects.filter(date__lte=current_date).order_by('-date')
    latest_news = News.objects.order_by('-date')[:4]
    paginator = Paginator(news_list, 10)  # Показывать 10 записей на странице
    page = request.GET.get('page')
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        # Если параметр страницы не является целым числом, отображаем первую страницу
        news = paginator.page(1)
    except EmptyPage:
        # Если страница находится за пределами допустимых значений (например, 9999),
        # отображаем последнюю страницу результатов
        news = paginator.page(paginator.num_pages)
    categories = Category.objects.all()  # Получаем все категории
    tags = Tag.objects.all()  # Получаем все теги
    return render(request, 'news/news.html', {'news': news, 'categories': categories, 'tags': tags, 'latest_news': latest_news})

def category_detail(request, pk):
    try:
        category = Category.objects.get(pk=pk)
        news_in_category = News.objects.filter(category=category)
        categories = Category.objects.all()
        latest_news = News.objects.order_by('-date')[:4]
        tags = Tag.objects.all()  # Получаем все теги
    except Category.DoesNotExist:
        raise Http404("Категория не найдена")
    return render(request, 'news/category-news.html', {'category': category, 'news_in_category': news_in_category, 'categories': categories, 'tags': tags, 'latest_news': latest_news})

def tag_detail(request, pk):
    try:
        tag = Tag.objects.get(pk=pk)
        news_in_tag = News.objects.filter(tags=tag)  # Фильтруем записи по выбранному тегу
        tags = Tag.objects.all()  # Получаем все теги (для отображения списка тегов)
        categories = Category.objects.all()
        latest_news = News.objects.order_by('-date')[:4]
    except Tag.DoesNotExist:
        raise Http404("Тег не найден")
    return render(request, 'news/tag-news.html', {'categories': categories, 'tag': tag, 'news_in_tag': news_in_tag, 'tags': tags, 'latest_news': latest_news})

class NewsDetailView(DetailView):
    model = News
    template_name = 'news/details-news.html'
    context_object_name = 'news_post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news_perent'] = self.object  # передаем объект News в контекст
        context['categories'] = Category.objects.all()
        context['tags'] = Tag.objects.all()
        context['latest_news'] = News.objects.order_by('-date')[:4]
        return context


def search_view(request):
    query = request.GET.get('q')
    if query:
        news_results = News.objects.filter(Q(title__icontains=query) | Q(excerpt__icontains=query))
    else:
        news_results = None
    return render(request, 'main/include/search.html', {'news_results': news_results, 'query': query})



def import_data_view(request):
    return render(request, 'admin/import_data.html')


class AddReviews(View):
    def post(self, request, pk):
        review_form = ReviewsForm(request.POST)

        if review_form.is_valid():
            review = review_form.save(commit=False)
            news_object = get_object_or_404(News, pk=pk)
            review.news_perent = news_object
            review.save()
            print("Отзыв сохранен успешно!")

        return HttpResponseRedirect(reverse('news-details', kwargs={'pk': pk}))


class AddResponse(View):
    def post(self, request, pk):
        response_form = ResponseForm(request.POST, request.FILES)

        if response_form.is_valid():
            parent_review_id = request.POST['parent_review_id']
            news_perent_res_id = request.POST['news_perent_res']

            parent_review = get_object_or_404(reviews, pk=parent_review_id)
            news_perent = get_object_or_404(News, pk=news_perent_res_id)

            response = response_form.save(commit=False)
            response.parent_review_res = parent_review
            response.news_perent_res = news_perent
            response.save()
            print("Ответ на отзыв сохранен успешно!")

        return HttpResponseRedirect(reverse('news-details', kwargs={'pk': pk}))

