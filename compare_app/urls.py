from django.urls import path, include
from .views import *

app_name = "compare_app"

urlpatterns =[
    path('one_to_one/<int:first_id>to<int:second_id>on<slug:title>', OneToOneView.as_view()),
    path('period/for<int:id>from<slug:start_period>to<slug:end_period>on<slug:title>', WorksToPeriodView.as_view()),
]