# Generated by Django 4.1.7 on 2023-04-03 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StayFit', '0008_hexercise_video_s_exercise_video_yoga_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('image', models.ImageField(upload_to='product_images')),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
