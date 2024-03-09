from django.contrib import admin
from .models import Setting, Category, Image

@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):
	list_display = ['title', 'description']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ['title']

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
	list_display = ['category', 'image']