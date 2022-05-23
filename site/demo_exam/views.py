from braces.views import LoginRequiredMixin

from django.views.generic.base import TemplateView
from django.views.generic import ListView

# locale imports
from library.models import BookModel

from .models import (
    ResultModel,
    DemoExamInfoModel,
    DemoExamDocModel,
    DemoExamMontageModel,
    DemoExamProgramModel,
    DemoExamTroubleShootingModel,
)


class InfoDemoExamView(LoginRequiredMixin, ListView):
    model = DemoExamInfoModel
    ordering = "filter_num"
    context_object_name = "contents"

    template_name = 'demo_exam/demo_exam_info.html'


class DocDemoExamView(LoginRequiredMixin, ListView):
    model = DemoExamDocModel
    ordering = "filter_num"
    context_object_name = "contents"

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


class MontageDemoExamView(LoginRequiredMixin, ListView):
    model = DemoExamMontageModel
    ordering = "filter_num"
    context_object_name = "contents"

    template_name = "demo_exam/demo_exam_montage.html"


class ProgrammingDemoExamView(LoginRequiredMixin, ListView):
    model = DemoExamProgramModel
    ordering = "filter_num"
    context_object_name = "contents"

    template_name = "demo_exam/demo_exam_programming.html"


class TroubleShootingDemoExamView(LoginRequiredMixin, ListView):
    model = DemoExamTroubleShootingModel
    ordering = "filter_num"
    context_object_name = "contents"

    template_name = "demo_exam/demo_exam_troubleshooting.html"
