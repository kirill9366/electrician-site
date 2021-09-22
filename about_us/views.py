from django.views.generic.base import TemplateView

# locale imports
from .models import ContactInfoModel


class AboutUsView(TemplateView):
    template_name = 'about_us.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['about_us'] = ContactInfoModel.objects.get()

        return context
