from django.urls import path

# locale imports
from .views import SignupView

urlpatterns = [
    path(
        'signup/',
        SignupView.as_view(),
        name='signup',
    ),

]
