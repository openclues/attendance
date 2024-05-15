from rest_framework import serializers
from .models import Instructor, Student, UserAccount


class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = (
            'first_name', 'last_name', 'username', 'email', 'date_joined',
        )


class InstructorSerializer(serializers.ModelSerializer):
    user = UserAccountSerializer(read_only=True)

    class Meta:
        model = Instructor
        fields = '__all__'
