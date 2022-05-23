from django.contrib import admin

# Register your models here.
from .models import (
    DemoExamInfoModel,
    DemoExamDocModel,
    DemoExamMontageModel,
    DemoExamProgramModel,
    DemoExamTroubleShootingModel,
)

admin.site.register(DemoExamInfoModel)
admin.site.register(DemoExamDocModel)
admin.site.register(DemoExamMontageModel)
admin.site.register(DemoExamProgramModel)
admin.site.register(DemoExamTroubleShootingModel)
