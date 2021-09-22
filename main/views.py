from django.views.generic import ListView

# locale imports
from news.models import NewsItemModel


class MainView(ListView):
    model = NewsItemModel
    context_object_name = 'news'
    queryset = NewsItemModel.objects.all()[:3]

    template_name = 'main.html'
