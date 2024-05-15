# Generated by Django 4.2.13 on 2024-05-15 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_alter_session_attended'),
        ('useraccount', '0003_remove_student_courses'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='courses',
            field=models.ManyToManyField(blank=True, related_name='students', to='course.course'),
        ),
    ]
