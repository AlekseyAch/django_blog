from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from mptt.models import MPTTModel, TreeForeignKey
from django.utils import timezone


class works(models.Model):
	titleWorks = models.CharField('Название услуги', max_length=250)
	slug = models.SlugField('Ссылка', max_length=250, blank=True, help_text="Заполняется автоматически")

	category = models.ForeignKey(
		'WorksCategory',
		verbose_name='Категория',
		on_delete=models.SET_NULL,
		null=True,
		default=1
	)

	imgWorks = models.ImageField('Главное изображение', upload_to='works/')

	clientWorks = models.CharField('Клиент/Компания', max_length=500)
	dateWorks = models.DateField('Дата старта проекта')
	dateWorksTy = models.DateField('Дата завершения проекта')
	linkWorks = models.URLField('Ссылка на проект')

	textWorks = RichTextField('Первое описание проекта')

	stepsWorks = RichTextField('Текст после заголовока что было сделано')

	resultWorks = RichTextField('Текст после заголовока результаты проекта')

	class Meta:
		verbose_name = 'Проекты'
		verbose_name_plural = 'Проект'

	def __str__(self):
		return self.titleWorks



class WorksGallery(models.Model):
	gallery = models.ForeignKey(
		works,
		related_name='gallery',
		verbose_name='Галерея проекта',
		on_delete=models.CASCADE
	)
	imgWorksGallery = models.ImageField('Главное изображение', upload_to='works/')

	class Meta:
		verbose_name = 'Галерея проекта'
		verbose_name_plural = 'Галерея проекта'


class WorksCategory(MPTTModel):
    WorksCategoryItem = models.CharField('Название категории', max_length=500)
    slug = models.SlugField('Ссылка', max_length=250, blank=True)
    parent = models.ForeignKey(
        'self',
        verbose_name='Категории',
        related_name="children",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None
    )

    class Meta:
        verbose_name = 'Категория проектов'
        verbose_name_plural = 'Категории проектов'

    def __str__(self):
	    return self.WorksCategoryItem

    class MPTTMeta:
        order_insertion_by = ['WorksCategoryItem']
