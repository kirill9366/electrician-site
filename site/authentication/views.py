from django.views.generic import FormView
from django.shortcuts import redirect
from django.contrib.auth import logout

# locale imports
from .forms import SignUpForm


class SignUpView(FormView):
    form_class = SignUpForm
    success_url = '/'

    template_name = 'authentication/signup.html'

    def form_valid(self, form):
        new_user = form.save(commit=False)
        new_user.set_password(form.cleaned_data['password'])
        new_user.save()

        new_user.addinfo.full_name = form.cleaned_data['full_name']
        new_user.addinfo.course_num = form.cleaned_data['course_num']
        new_user.addinfo.save()

        return redirect('main')


def logout_view(request):
    logout(request)
    return redirect('main')
