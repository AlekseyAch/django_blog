from django.db import models
from ckeditor.fields import RichTextField
from django.core.exceptions import ValidationError


class ContactsModal(models.Model):
	"""Класс модели обратной связи"""
	email = models.EmailField('Почта')
	name = models.CharField('ФИО', max_length=150)
	massage = models.TextField('Сообщение', max_length=5000)
	create_add = models.DateTimeField('Дата и время заявки', auto_now_add=True)

	def __str__(self):
		return f"{self.name} {self.email}"

	class Meta:
		verbose_name = 'Заявка с формы'
		verbose_name_plural = 'Заявки с формы'

class ContactInfo(models.Model):
	"""Класс контактных данных"""
	title_block = models.CharField('Заголовок над формой', max_length=500)
	phone = models.IntegerField('Номер телефона')
	email_site = models.EmailField('Почта на сайте')
	adress_local = models.CharField('Адрес указанный на сайте', max_length=1000)

	def formatted_phone(self):
		# Преобразуем номер телефона в строку
		phone_str = str(self.phone)
		# Удаляем все символы, кроме цифр
		digits = ''.join(filter(str.isdigit, phone_str))
		# Форматируем номер телефона по требуемой маске
		formatted_phone = '+7 ({}) {}-{}-{}'.format(
			digits[:3], digits[3:6], digits[6:8], digits[8:])
		return formatted_phone

	def __str__(self):
		return self.title_block

	class Meta:
		verbose_name = 'Данные для страниц'
		verbose_name_plural = 'Данные для страниц'

class socialLinks(models.Model):
	"""Социальне сети сайта"""
	ikons = models.CharField(
		'Класс иконки',
		max_length=200,
		help_text= "Иконки берем из этого пака <a href=\"https://icons.getbootstrap.com/\" target=\"blank\"> Иконки для сайта</a>"
	)
	link = models.URLField(
		'Ссылка на соц сеть',
		help_text="Ссылка вставляется полная"
	)

	class Meta:
		verbose_name = 'Социальные сети'
		verbose_name_plural = 'Социальные сети'


class hiroBlock(models.Model):
	"""Первый блок, главный экран страницы"""
	mini_text = models.TextField('Текст над заголовком', max_length=200)
	mini_text_str = models.TextField('Текст над заголовком вторая строка', max_length=200)
	mini_text_link = models.URLField('Ссылка на первый текст', max_length=200)
	h1_site = models.TextField('Заголовок сайта', max_length=200)
	color_text = models.TextField('Текст с цветом', help_text="Важно! Заполнять только одно слово")
	image = models.ImageField('Изображение на первом экране', upload_to='home/', default='default/bsmall1.png')
	link_yutube = models.URLField('Ссылка на ютуб видео')

	class Meta:
		verbose_name = 'Первый экран'
		verbose_name_plural = 'Первый экран'

	def __str__(self):
		return self.h1_site

	def clean(self):
		if hiroBlock.objects.exists() and not self.pk:
			raise ValidationError("Можно создать только одну запись для этой модели")


class galleryHomePage(models.Model):
	galery = models.ForeignKey(
		hiroBlock,
		related_name='galleries',
		verbose_name='Блок',
		on_delete=models.CASCADE
	)
	image = models.ImageField('Изображение', upload_to='block-ty-galery/')

	class Meta:
		verbose_name = 'Изображение'
		verbose_name_plural = 'Галереи'


class ourAwards(models.Model):
	title = models.TextField('Название компании', max_length=250)
	text = models.TextField('Описание в нескольких словах', max_length=200, help_text="Важно! Заполнять только одно/два слова")
	yar = models.IntegerField('Год работы')

	class Meta:
		verbose_name = 'Одна компания'
		verbose_name_plural = 'Где работал'

class WorkStepsHomePage(models.Model):
	TitleWorkSteps = models.TextField('Заголовок блока Этапы работы', max_length=250)
	SubTitleWorkSteps = models.CharField('Подзаголовок который стоит над заголовоком', max_length=200)
	class Meta:
		verbose_name = 'Блок шагов'
		verbose_name_plural = 'Шаги работы над проектом'

class OneStepHomePage(models.Model):
	OneStep = models.ForeignKey(
		WorkStepsHomePage,
		related_name='OneStep',
		verbose_name='Блок',
		on_delete=models.CASCADE
	)
	TitleOneStep = models.CharField('Заголовок этапа', max_length=50)
	TextOneStep = models.TextField('Описание этапа', max_length=500)
	ListOneStep = RichTextField('Пункты списка', help_text="Нужно вставлять верный код!")


class footerInfo(models.Model):
	"""Заполнение подвала"""
	bigText = models.CharField('Большой текст из подвала', max_length=250)
	footerDesc = models.TextField('Описание сайта в подвале', max_length=500)
	copyrightText = RichTextField('Копирайт', help_text="Можно вставлять ссылки")

	def __str__(self):
		return self.bigText


	class Meta:
		verbose_name = 'Информация в подвале'
		verbose_name_plural = 'Информация в подвале'

class polysiFooter(models.Model):
	polysiFooterItem = models.ForeignKey(
		footerInfo,
		related_name="Политика",
		verbose_name="Политики конфиденциальности",
		on_delete=models.CASCADE
	)
	polysiTitle = models.CharField('Название страницы политики', max_length=250)
	polysiUrl = models.URLField('Ссылка на страницу политики', max_length=250)