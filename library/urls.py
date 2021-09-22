from django.urls import path

# locale imports
from .views import LibraryView

urlpatterns = [
    path('library/', LibraryView.as_view(), name='library'),
]
