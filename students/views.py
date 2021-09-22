from django.views.generic import ListView
from django.views.generic.detail import DetailView


# locale imports
from .models import StudentModel


class StudentsView(ListView):
    model = StudentModel
    context_object_name = 'students'
    paginate_by = 9

    template_name = 'students/students.html'


class StudentDetailView(DetailView):
    model = StudentModel

    template_name = 'students/student_page.html'
