from django.urls import path
from .views import course_list, course_detail, enroll_student, filter_courses

urlpatterns = [
    path('courses/', course_list),
    path('courses/<int:pk>/', course_detail),
    path('enrollments/', enroll_student),
    path('courses/filter/', filter_courses, name='filter_courses'),
]
