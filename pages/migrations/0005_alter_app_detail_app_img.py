# Generated by Django 4.2.11 on 2024-05-05 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_app_detail_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app_detail',
            name='app_img',
            field=models.ImageField(upload_to='app_images/'),
        ),
    ]
