# Generated by Django 4.2.13 on 2024-05-15 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
        ('useraccount', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='courses',
            field=models.ManyToManyField(blank=True, related_name='students', to='course.course'),
        ),
        migrations.AddField(
            model_name='student',
            name='years',
            field=models.ManyToManyField(blank=True, related_name='students', to='course.year'),
        ),
    ]
