from django.contrib import admin

# locale imports
from .models import BookModel, CategoryModel

admin.site.register(CategoryModel)
admin.site.register(BookModel)
