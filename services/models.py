from django.db import models
from ckeditor.fields import RichTextField


class oneServices(models.Model):
	directionServices = models.CharField('Направление услуги', max_length=250)
	titleServices = models.CharField('Название услуги', max_length=250)
	imgServices = models.ImageField('Изображение услуги', upload_to='services_images/')
	descriptionServices = models.TextField('Краткое описание услуги', max_length=250)
	textServices = RichTextField('Текст услуги')
	videoServices = models.URLField('Ссылка на видео в попап окне')
	imgVideoServices = models.ImageField('Картинка заглушка видео', upload_to='services_images/')
	titleQveschenServices = models.CharField('Заголовок блока вопросы и ответы', max_length=250)

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