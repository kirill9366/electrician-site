from django.contrib import admin

# locale imports
from .models import (
    CourseModel,
    CourseProjectModel,
)

admin.site.register(CourseModel)
admin.site.register(CourseProjectModel)
