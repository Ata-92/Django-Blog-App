# Generated by Django 3.2.5 on 2021-07-28 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_app', '0003_alter_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=25),
        ),
    ]
