from braces.views import LoginRequiredMixin

from django.views.generic.base import TemplateView
from django.views.generic import ListView

# locale imports
from .models import ResultModel

from library.models import BookModel


class InfoDemoExamView(LoginRequiredMixin, TemplateView):
    template_name = 'demo_exam/demo_exam_info.html'


class DocDemoExamView(LoginRequiredMixin, TemplateView):
    template_name = 'demo_exam/demo_exam_documentation.html'


class LibDemoExamView(LoginRequiredMixin, ListView):
    model = BookModel
    context_object_name = 'books'

    template_name = 'demo_exam/demo_exam_library.html'


class DatesDemoExamView(LoginRequiredMixin, TemplateView):
    template_name = 'demo_exam/demo_exam_calendar.html'


class ResDemoExamView(LoginRequiredMixin, ListView):
    model = ResultModel
    context_object_name = 'results'

    template_name = 'demo_exam/demo_exam_results.html'


class MontageDemoExamView(LoginRequiredMixin, TemplateView):
    template_name = "demo_exam/demo_exam_montage.html"


class ProgrammingDemoExamView(LoginRequiredMixin, TemplateView):
    template_name = "demo_exam/demo_exam_programming.html"


class TroubleShootingDemoExamView(LoginRequiredMixin, TemplateView):
    template_name = "demo_exam/demo_exam_troubleshooting.html"
