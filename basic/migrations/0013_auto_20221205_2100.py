# Generated by Django 3.2.9 on 2022-12-05 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0012_auto_20221205_2029'),
    ]

    operations = [
        migrations.AddField(
            model_name='company_hired',
            name='hire_id',
            field=models.TextField(default='noname', max_length=2000),
        ),
        migrations.AddField(
            model_name='company_hired',
            name='name',
            field=models.TextField(default='noname', max_length=2000),
        ),
    ]
