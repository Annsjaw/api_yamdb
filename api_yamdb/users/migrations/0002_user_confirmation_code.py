# Generated by Django 2.2.16 on 2022-08-29 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='confirmation_code',
            field=models.CharField(blank=True, max_length=30, null=True, unique=True, verbose_name='Код подтверждения'),
        ),
    ]
