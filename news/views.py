from django.views.generic import ListView
from django.views.generic.detail import DetailView

# locale imports
from .models import NewsItemModel


class NewsView(ListView):
    model = NewsItemModel
    context_object_name = 'news'
    paginate_by = 6

    template_name = 'news/news.html'


class NewsDetailView(DetailView):
    model = NewsItemModel

    template_name = 'news/news_item.html'
