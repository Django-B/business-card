from django.db import models
from django.conf import settings

class Setting(models.Model):
	tab_title = models.CharField(max_length=200, verbose_name='Имя во вкладке', default='Визитка')
	title = models.CharField(max_length=200, verbose_name='Заголовок')
	subtitle = models.CharField(max_length=200, null=True, blank=True, verbose_name='Подзаголовок')
	description = models.CharField(max_length=200, null=True, blank=True, verbose_name='Описание')
	contact1 = models.CharField(max_length=200, null=True, blank=True, verbose_name='Контакт 1')
	contact2 = models.CharField(max_length=200, null=True, blank=True, verbose_name='Контакт 2')
	contact3 = models.CharField(max_length=200, null=True, blank=True, verbose_name='Контакт 3')
	image = models.ImageField(null=True, blank=True, verbose_name='Фоновое изображение')

	class Meta:
		verbose_name = 'Настройки'
		verbose_name_plural = 'Настройки'

class Category(models.Model):
	title = models.CharField(max_length=200, verbose_name='Имя категории')

	class Meta:
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'

	def __str__(self):
		return self.title

class Image(models.Model):
	image = models.ImageField(verbose_name='Изображение')
	category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True, blank=False, verbose_name='Категория')

	class Meta:
		verbose_name = 'Изображение'
		verbose_name_plural = 'Изображения'

