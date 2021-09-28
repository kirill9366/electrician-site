from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView


# locale imports
from .models import PracticeModel


class PracticeView(ListView):
    model = PracticeModel
    context_object_name = 'practice_list'

    template_name = 'practice/practice.html'


class PracticeDetailView(DetailView):
    model = PracticeModel

    template_name = 'practice/practice_item.html'
