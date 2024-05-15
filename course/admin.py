from django.contrib import admin

# Register your models here.
from .models import Course, Year, Semester, Session


class SemesterInline(admin.TabularInline):
    model = Semester
    extra = 1


class YearAdmin(admin.ModelAdmin):
    inlines = [SemesterInline]


class SessionInline(admin.TabularInline):
    model = Session
    extra = 1


class CourseAdmin(admin.ModelAdmin):
    inlines = [SessionInline]


admin.site.register( Course, CourseAdmin)

admin.site.register(Year)
admin.site.register(Semester)
