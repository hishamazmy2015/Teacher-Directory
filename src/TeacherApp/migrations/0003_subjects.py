# Generated by Django 3.1.5 on 2021-01-25 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TeacherApp', '0002_auto_20210125_0650'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('SubjectsId', models.AutoField(primary_key=True, serialize=False)),
                ('SubjectsName', models.CharField(max_length=100)),
            ],
        ),
    ]
