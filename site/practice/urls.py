from django.urls import path

# locale imports
from .views import PracticeView, PracticeDetailView

urlpatterns = [
    path('practice/', PracticeView.as_view(), name='practice'),
    path(
        'practice/<int:pk>/',
        PracticeDetailView.as_view(),
        name='practice_item',
    ),
]
