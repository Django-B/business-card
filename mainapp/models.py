from django.db import models
from django.conf import settings

class Setting(models.Model):
	title = models.CharField(max_length=200, verbose_name='Заголовок')
	description = models.CharField(max_length=200, null=True, blank=True, verbose_name='Описание')
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

