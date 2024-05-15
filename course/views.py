from datetime import timezone, datetime

from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from course.models import Session, Year
from course.serializers import SessionSerializer, YearSerializer
from useraccount.models import Student


# Create your views here.
class TodaysSessionsApiView(generics.ListAPIView):
    serializer_class = SessionSerializer

    def get_queryset(self):
        user = self.request.user
        # student = Student.objects.filter(user=user)
        print(user)
        return Session.objects.filter(date__exact=datetime.today().date(), course__students__user__in=[user])


class SessionsHistoryApiView(generics.ListAPIView):
    serializer_class = SessionSerializer

    def get_queryset(self):
        user = self.request.user
        return Session.objects.filter(course__students__user__in=[user])


class StudentYearsApiView(generics.ListAPIView):
    serializer_class = YearSerializer

    def get_queryset(self):
        user = self.request.user


        return Year.objects.filter(
            students__user__in=[user.id]
        )
