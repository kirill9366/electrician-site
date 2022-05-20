from braces.views import LoginRequiredMixin

from django.views.generic import ListView
from django.views.generic.detail import DetailView


# locale imports
from .models import PracticeModel


class PracticeView(LoginRequiredMixin, ListView):
    model = PracticeModel
    context_object_name = 'practice_list'

    template_name = 'practice/practice.html'


class PracticeDetailView(LoginRequiredMixin, DetailView):
    model = PracticeModel

    template_name = 'practice/practice_item.html'
