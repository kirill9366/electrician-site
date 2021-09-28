from django.contrib import admin

# locale imports
from .models import NewsItemModel, ParagraphModel


admin.site.register(NewsItemModel)
admin.site.register(ParagraphModel)
