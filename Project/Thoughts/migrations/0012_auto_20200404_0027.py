# Generated by Django 3.0.3 on 2020-04-04 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Thoughts', '0011_auto_20200404_0027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='comments',
            field=models.ManyToManyField(null=True, to='Thoughts.Comment'),
        ),
    ]
