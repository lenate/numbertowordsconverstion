from django.urls import path
from .import views as v

urlpatterns = [
    
    path("", v.task, name="task"),
    path("result", v.convert, name="result")
]