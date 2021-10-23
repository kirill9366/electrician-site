from django.urls import path
from django.contrib.auth.views import LoginView

# locale imports
from .views import SignUpView, logout_view

from .forms import SignInForm

urlpatterns = [
    path(
        'sign-up/',
        SignUpView.as_view(),
        name='signup',
    ),
    path(
        'sign-in/',
        LoginView.as_view(
            template_name='authentication/signin.html',
            form_class=SignInForm,
            success_url='main',
        ),
        name='signin',
    ),
    path(
        'logout/',
        logout_view,
        name='logout',
    ),
]
