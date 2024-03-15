from django.db import models
from ckeditor.fields import RichTextField
from django.db.models.signals import post_save
from django.utils.text import slugify
from django.dispatch import receiver
from django.urls import reverse

class oneServices(models.Model):
	directionServices = models.CharField('Направление услуги', max_length=250)
	slug = models.SlugField('Ссылка', max_length=250, blank=True)
	titleServices = models.CharField('Название услуги', max_length=250)
	imgServices = models.ImageField('Изображение услуги', upload_to='services_images/')
	descriptionServices = models.TextField('Краткое описание услуги', max_length=250)
	textServices = RichTextField('Текст услуги')
	videoServices = models.URLField('Ссылка на видео в попап окне')
	imgVideoServices = models.ImageField('Картинка заглушка видео', upload_to='services_images/')
	titleQveschenServices = models.CharField('Заголовок блока вопросы и ответы', max_length=250)
	sortNumber = models.IntegerField('Поле сортировки', default=1)


	def save(self, *args, **kwargs):
		if not self.slug:  # Проверяем, было ли уже заполнено поле Slug
			self.slug = slugify(self.titleServices)  # Создаем слаг из названия
		super().save(*args, **kwargs)

	class Meta:
		ordering = ['sortNumber']

	def __str__(self):
		return self.titleServices


	class Meta:
		verbose_name = 'Услуги'
		verbose_name_plural = 'Одна услуга'

class accardionServices(models.Model):
	accardionServicesItem = models.ForeignKey(
		oneServices,
		verbose_name="Вопросы и ответы",
		related_name="Вопрос",
		on_delete=models.CASCADE
	)
	titleAccardionServicesItem = models.CharField('Заголовок вопроса', max_length=250)
	textAccardionServicesItem = models.TextField('Ответ на вопрос')

	def __str__(self):
		return self.titleAccardionServicesItem


@receiver(post_save, sender=oneServices)
def update_sort_number(sender, instance, created, **kwargs):
    if created:  # Проверяем, был ли объект только что создан
        latest_sort_number = oneServices.objects.latest('sortNumber').sortNumber
        instance.sortNumber = latest_sort_number + 1
        instance.save()