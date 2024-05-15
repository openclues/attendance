from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        print("Called")
        password = make_password(password=password)
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        print("Created")
        user.save(using=self._db)
        return user


class UserAccount(AbstractUser):
    address = models.CharField(max_length=120, blank=True, null=True)
    objects = CustomUserManager()


class Student(models.Model):
    student_id = models.CharField(max_length=120, blank=True, null=True)
    user = models.OneToOneField(UserAccount, on_delete=models.CASCADE)
    years = models.ManyToManyField('course.Year', related_name="students", blank=True)
    courses = models.ManyToManyField('course.Course', related_name="students", blank=True)

    def __str__(self):
        return self.student_id


class Instructor(models.Model):
    instructor_id = models.IntegerField(unique=True, null=True, blank=True)
    user = models.OneToOneField(UserAccount, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.instructor_id)