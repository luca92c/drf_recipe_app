# Generated by Django 3.0.5 on 2020-04-26 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0008_auto_20200426_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=255),
        ),
    ]
