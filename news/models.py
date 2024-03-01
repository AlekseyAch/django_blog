from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.utils.translation import gettext_lazy as _
from django import forms

from mptt.models import MPTTModel, TreeForeignKey

class News(models.Model):
    title = models.CharField('Название', max_length=100)
    slug = models.SlugField('Ссылка', max_length=250, blank=True)
    excerpt = models.CharField('Анонс', max_length=255, blank=True, null=True)

    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        default=1)
    date = models.DateTimeField(default=timezone.now)
    tags = models.ManyToManyField(
        'Tag',
        verbose_name='Теги')
    category = models.ForeignKey(
        'Category',
        verbose_name='Категория',
        on_delete=models.SET_NULL,
        null=True,
        default=1)
    text_blocks = RichTextField(
        'Текстовые блоки',
        blank=True,
        null=True)
    text_img = models.ImageField(
        'Главное изображение записи',
        upload_to='news_images/',
        default='default/bblog1.png')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Запись блога'
        verbose_name_plural = 'Записи блога'

class Gallery(models.Model):
    news = models.ForeignKey(
        News,
        related_name='galleries',
        verbose_name='Новость',
        on_delete=models.CASCADE
    )
    image = models.ImageField('Изображение', upload_to='news_galleries/')

    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галереи'

class Category(MPTTModel):
    title = models.CharField('Заголовок', max_length=50)
    created_at = models.DateTimeField('Дата создания', default=timezone.now)
    slag = models.SlugField('Ссылка', max_length=250, default=0)
    parent = TreeForeignKey(
        'self',
        related_name="children",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория записи'
        verbose_name_plural = 'Категории записей'

    def get_news(self):
        return News.objects.filter(category=self)

    class MPTTMeta:
        order_insertion_by = ['title']



class Tag(models.Model):
    title = models.CharField('Теги поста:', max_length=50)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тег записи'
        verbose_name_plural = 'Теги записей'

    def get_news(self):
        return self.news_set.all()

class reviews(models.Model):
    name = models.CharField('Имя оставившего отзыв', max_length=100)
    email = models.EmailField('Почта')
    text_rev = RichTextField('Отзыв', blank=True, null=True)
    news_perent = models.ForeignKey('News', verbose_name='Новость', on_delete=models.CASCADE)
    vork_user = models.CharField('Должность', max_length=100, default=1)

    def __str__(self):
        return f"{self.name} - {self.news_perent}"

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class Response(models.Model):
    name_res = models.CharField('Имя оставившего ответ', max_length=100)
    email_res = models.EmailField('Почта')
    text_rev_res = models.TextField('Ответ', blank=True, null=True)
    parent_review_res = models.ForeignKey(
        reviews,
        verbose_name='Родительский отзыв',
        on_delete=models.CASCADE,
        null=True,
        default=1
    )
    news_perent_res = models.ForeignKey(
        'News',
        verbose_name='Новость',
        on_delete=models.CASCADE,
        null=True,
        default=1
    )
    vork_user_res = models.CharField('Должность', max_length=100, null=True)

    def __str__(self):
        return f"{self.id} - {self.name_res}"  # Или замените name_res на другое поле, которое вы хотите отображать
    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

def count_reviews_for_post(post_id):
    post = News.objects.get(pk=post_id)
    num_reviews = post.reviews_set.count()
    return num_reviews