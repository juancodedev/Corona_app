# Generated by Django 3.0.6 on 2020-05-17 01:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('corona_app', '0005_noticias_hora'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='noticias',
            name='hora',
        ),
    ]
