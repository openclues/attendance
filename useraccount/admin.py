from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import UserAccount, Instructor, Student


# Register your models here.


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass


@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    pass

admin.site.register(UserAccount, UserAdmin)