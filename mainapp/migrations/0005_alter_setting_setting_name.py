# Generated by Django 5.0.3 on 2024-03-09 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_alter_category_title_alter_image_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='setting_name',
            field=models.CharField(default='default', editable=False, max_length=100, unique=True, verbose_name='Название настроек'),
        ),
    ]