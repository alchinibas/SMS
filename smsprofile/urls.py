from . import views
from django.urls import path

app_name="smsprofile"

urlpatterns = [
    path('student/register/',views.register_student, name="student_register")
]
