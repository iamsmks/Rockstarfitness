# Generated by Django 4.1.7 on 2023-03-29 07:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('StayFit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GExercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('difficulty_level', models.IntegerField()),
                ('muscle_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StayFit.musclegroup')),
            ],
        ),
        migrations.CreateModel(
            name='HExercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('difficulty_level', models.IntegerField()),
                ('muscle_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StayFit.musclegroup')),
            ],
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='pt_Exercises',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('difficulty_level', models.IntegerField()),
                ('muscle_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StayFit.musclegroup')),
            ],
        ),
        migrations.CreateModel(
            name='S_Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('difficulty_level', models.IntegerField()),
                ('muscle_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StayFit.musclegroup')),
            ],
        ),
        migrations.CreateModel(
            name='Yoga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('difficulty_level', models.IntegerField()),
                ('Benefitss', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StayFit.musclegroup')),
            ],
        ),
        migrations.DeleteModel(
            name='Exercise',
        ),
        migrations.AlterField(
            model_name='workout',
            name='exercises',
            field=models.ManyToManyField(to='StayFit.gexercise'),
        ),
    ]