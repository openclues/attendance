# Generated by Django 4.2.13 on 2024-05-15 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0002_student_courses_student_years'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='courses',
        ),
    ]
