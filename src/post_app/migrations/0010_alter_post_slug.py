# Generated by Django 3.2.5 on 2021-07-30 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_app', '0009_auto_20210730_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=10),
        ),
    ]
