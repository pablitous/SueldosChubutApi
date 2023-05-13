from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("salary/", views.get_salary, name="get_salary"),
    path("organisms/", views.get_organisms, name="get_organisms"),
]