# Generated by Django 3.0.3 on 2020-03-01 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExtendsUserModel', '0003_auto_20200301_0819'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='first name'),
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
    ]
