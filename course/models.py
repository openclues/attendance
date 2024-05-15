from django.db import models

from useraccount.models import Instructor, Student


# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    code = models.CharField(max_length=100, blank=True, null=True)
    semester = models.ForeignKey('Semester', on_delete=models.CASCADE, blank=True, null=True)

    # def __str__(self):
    #     return self.name


class Year(models.Model):
    name = models.CharField(max_length=100, unique=True)
    #
    # def __str__(self):
    #     return self.name


class Semester(models.Model):
    name = models.CharField(max_length=100, unique=True)
    year = models.ForeignKey(Year, on_delete=models.CASCADE, related_name='semesters')

    # def __str__(self):
    #     return self.name


class Session(models.Model):
    lecture_title = models.CharField(max_length=100, unique=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    hall = models.CharField(max_length=100, unique=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    date = models.DateField()
    attended = models.ManyToManyField(Student, related_name='attended', blank=True, null=True)

    def __str__(self):
        return self.lecture_title

    @property
    def have_to_attend(self):
        return self.course.students.all()




