from django.contrib import admin

# locale imports
from .models import NewsItemModel, NewsParagraphModel


admin.site.register(NewsItemModel)
admin.site.register(NewsParagraphModel)
