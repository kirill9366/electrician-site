from django.urls import path

# locale imports
from .views import CourseProjectsView, CourseProjectDetailView

urlpatterns = [
    path(
        'student-projects/',
        CourseProjectsView.as_view(),
        name='course_projects',
    ),
    path(
        'student-projects/<int:pk>/',
        CourseProjectDetailView.as_view(),
        name='course_project',
    ),
]
