from django.contrib import admin

# locale imports
from .models import (
    CourseModel,
    CourseParagraphModel,
    CourseProjectModel,
)

admin.site.register(CourseModel)
admin.site.register(CourseParagraphModel)
admin.site.register(CourseProjectModel)
