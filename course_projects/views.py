from django.views.generic import ListView
from django.views.generic.detail import DetailView

# locale imports
from .models import CourseModel, CourseProjectModel


class CourseProjectsView(ListView):
    model = CourseProjectModel
    context_object_name = 'course_projects'
    paginate_by = 9

    template_name = 'course_projects/course_projects.html'

    def get_queryset(self):

        if self.request.user.is_superuser:
            return self.model.objects.all()

        course = CourseModel.objects.get(
            number=self.request.user.addinfo.course_num
        )
        return self.model.objects.filter(course=course)


class CourseProjectDetailView(DetailView):
    model = CourseProjectModel

    template_name = 'course_projects/course_project.html'
