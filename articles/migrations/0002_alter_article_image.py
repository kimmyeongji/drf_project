# Generated by Django 4.1.3 on 2022-11-21 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, upload_to='%Y/%m/'),
        ),
    ]
