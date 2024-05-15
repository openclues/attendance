from rest_framework import serializers

from useraccount.serializers import InstructorSerializer
from .models import Course, Session, Year, Semester


class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semester
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    instructor = InstructorSerializer(read_only=True)

    class Meta:
        model = Course
        fields = '__all__'


class SessionSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True, many=False)

    class Meta:
        model = Session
        fields = '__all__'


class YearSerializer(serializers.ModelSerializer):
    semesters = SemesterSerializer(many=True, read_only=True)
    class Meta:
        model = Year
        fields = '__all__'
