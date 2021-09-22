from django.views.generic import ListView

# locale imports
from .models import BookModel


class LibraryView(ListView):
    model = BookModel
    context_object_name = 'books'

    template_name = 'library.html'
