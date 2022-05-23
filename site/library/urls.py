from django.urls import path

# locale imports
from .views import LibraryView, BooksView

urlpatterns = [
    path('library/', LibraryView.as_view(), name='library'),
    path('library/<int:pk>/', BooksView.as_view(), name='library_item'),
]
