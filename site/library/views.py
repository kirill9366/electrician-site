from braces.views import LoginRequiredMixin

from django.views.generic import ListView, DetailView

# locale imports
from .models import CategoryModel


class LibraryView(LoginRequiredMixin, ListView):
    model = CategoryModel
    context_object_name = 'categories'

    template_name = 'library/library.html'


class BooksView(LoginRequiredMixin, DetailView):
    model = CategoryModel

    template_name = 'library/library_item.html'
