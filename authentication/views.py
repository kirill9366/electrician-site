from django.views.generic import FormView

# locale imports
from .forms import SignupForm


class SignupView(FormView):
    form_class = SignupForm
    success_url = '/'

    template_name = 'authentication/signup.html'

    def form_valid(self, form):
        return super(SignupView, self).form_valid(form)
