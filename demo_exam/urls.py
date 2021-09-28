from django.urls import path

# locale imports
from .views import (
    InfoDemoExamView,
    DocDemoExamView,
    LibDemoExamView,
    DatesDemoExamView,
    ResDemoExamView,
)

urlpatterns = [
    path('demo-exam/', InfoDemoExamView.as_view(), name='demo_exam'),
    path('demo-exam/doc/', DocDemoExamView.as_view(), name='demo_exam_doc'),
    path(
        'demo-exam/lib/',
        LibDemoExamView.as_view(),
        name='demo_exam_library',
    ),
    path(
        'demo-exam/dates/',
        DatesDemoExamView.as_view(),
        name='demo_exam_dates',
    ),
    path(
        'demo-exam/res/',
        ResDemoExamView.as_view(),
        name='demo_exam_results',
    ),

]
