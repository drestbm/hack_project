from django.urls import path, include
from .views import *

app_name = "main"

urlpatterns =[
    path('', ServiceView.as_view()),
    path('index/', index),
    path('<int:pk>', ServiceByCompanyIdView.as_view()),
    path('<int:pk>/<slug:title>', ServiceByCompanyIdAndSlugView.as_view()),
    path('<int:pk>/<slug:title>/wrong', WrongServiceByCompanyIdAndSlugView.as_view()),
]