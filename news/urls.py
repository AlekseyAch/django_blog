from django.urls import path
from . import views
from .views import search_view

urlpatterns = [
    path('', views.news_str, name='news'),
    path('<int:pk>/', views.NewsDetailView.as_view(), name='news-details'),
    path('category/<int:pk>/', views.category_detail, name='category_detail'),
    path('tag/<int:pk>/', views.tag_detail, name='tag_detail'),
    path('search/', search_view, name='search'),
    path('reviews/<int:pk>/', views.AddReviews.as_view(), name='add_reviews'),
    path('reviews/response/<int:pk>/', views.AddResponse.as_view(), name='add_response'),
]
