# Generated by Django 5.0.3 on 2024-03-09 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_alter_category_options_alter_image_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='media/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/', verbose_name='Фоновое изображение'),
        ),
    ]