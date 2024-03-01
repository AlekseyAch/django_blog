from django.contrib import admin
from django.utils.html import format_html
from django.http import HttpResponseRedirect
from django.shortcuts import render
from news.models import News, Tag, Category, reviews, Response, Gallery
from .import_from_wordpress import import_wordpress_data
from mptt.admin import MPTTModelAdmin

admin.site.register(Category, MPTTModelAdmin)
admin.site.register(Tag)
class ResponseInline(admin.StackedInline):  # или admin.TabularInline для компактного отображения
    model = Response

@admin.register(reviews)
class ReviewAdmin(admin.ModelAdmin):
    inlines = [
        ResponseInline,
    ]

admin.site.register(Response)

class TagInline(admin.TabularInline):
    model = News.tags.through
    extra = 3

class GalleryInlineAdmin(admin.TabularInline):
    model = Gallery


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    inlines = [
        TagInline,
        GalleryInlineAdmin,
    ]
    list_display = (
        'title',
        'category',
        'display_tags',
        'display_thumbnail',
        'date'
    )
    readonly_fields = ['display_thumbnail']
    list_display_links = ('title',)
    list_per_page = 10
    list_filter = ('category', 'tags')
    search_fields = ['title', 'excerpt']
    prepopulated_fields = {'slug': ('title',)}

    def display_tags(self, obj):
        return ', '.join(tag.title for tag in obj.tags.all()) if obj.tags.exists() else 'Нет тегов'

    display_tags.short_description = 'Теги'

    def display_thumbnail(self, obj):
        if obj.text_img:
            return format_html('<img src="{}" width="100" />', obj.text_img.url)
        else:
            return 'No Image'

    display_thumbnail.short_description = 'Картинка записи'



    def copy_selected_news(self, request, queryset):
        selected_news = list(queryset.values())

        for news_data in selected_news:
            news_data.pop('id')
            News.objects.create(**news_data)

        self.message_user(request, f"{len(selected_news)} записей успешно скопировано.")

    copy_selected_news.short_description = "Копировать выбранные записи"

    actions = ['import_selected_news', 'copy_selected_news']













