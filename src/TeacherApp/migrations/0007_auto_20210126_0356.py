# Generated by Django 3.1.5 on 2021-01-26 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TeacherApp', '0006_auto_20210126_0325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='PhotoFileName',
            field=models.ImageField(default='21744.jpg', upload_to='resources'),
        ),
    ]