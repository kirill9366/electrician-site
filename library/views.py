from braces.views import LoginRequiredMixin

from django.views.generic import ListView

# locale imports
from .models import BookModel


class LibraryView(LoginRequiredMixin, ListView):
    model = BookModel
    context_object_name = 'books'

    template_name = 'library.html'
