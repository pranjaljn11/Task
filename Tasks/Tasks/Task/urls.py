#created urls.py for TASK app
from django.urls import path
from . import views


urlpatterns = [path('', views.Task.as_view(), name="Task"),
               path('', views.StopTask.as_view(), name="StopTask"),
               ]