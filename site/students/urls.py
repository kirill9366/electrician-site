from django.urls import path

# locale imports
from .views import StudentsView, StudentDetailView

urlpatterns = [
    path('students/', StudentsView.as_view(), name='students'),
    path('students/<int:pk>', StudentDetailView.as_view(), name='student'),
]
