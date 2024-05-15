from django.urls import path
from .views import TodaysSessionsApiView, SessionsHistoryApiView, StudentYearsApiView


urlpatterns = [
    path('', TodaysSessionsApiView.as_view(), name='today_sessions' ),
    path('history/', SessionsHistoryApiView.as_view(), name='sessions_history' ),
    path('student/year/',StudentYearsApiView.as_view(), name='student_years' ),
]