# Generated by Django 5.0.3 on 2024-03-09 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_rename_settings_setting'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='setting_name',
            field=models.CharField(default='default', editable=False, max_length=100),
        ),
    ]
