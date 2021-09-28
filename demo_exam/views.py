from django.views.generic.base import TemplateView
from django.views.generic import ListView

# locale imports
from .models import ResultModel

from library.models import BookModel


class InfoDemoExamView(TemplateView):
    template_name = 'demo_exam/demo_exam_info.html'


class DocDemoExamView(TemplateView):
    template_name = 'demo_exam/demo_exam_documentation.html'


class LibDemoExamView(ListView):
    model = BookModel
    context_object_name = 'books'

    template_name = 'demo_exam/demo_exam_library.html'


class DatesDemoExamView(TemplateView):
    template_name = 'demo_exam/demo_exam_calendar.html'


class ResDemoExamView(ListView):
    model = ResultModel
    context_object_name = 'results'

    template_name = 'demo_exam/demo_exam_results.html'
