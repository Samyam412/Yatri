# Generated by Django 4.0.1 on 2022-02-21 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_carouselimage_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='carouselImage2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image2', models.ImageField(upload_to='carouselImage2')),
            ],
        ),
    ]
