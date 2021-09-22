from django.views.generic import ListView
from django.views.generic.detail import DetailView

# locale imports
from .models import CourseProjectModel


class CourseProjectsView(ListView):
    model = CourseProjectModel
    context_object_name = 'course_projects'
    paginate_by = 9

    template_name = 'course_projects/course_projects.html'


class CourseProjectDetailView(DetailView):
    model = CourseProjectModel

    template_name = 'course_projects/course_project.html'
