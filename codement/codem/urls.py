from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name='index'),
    path("codement", views.codement_20, name='codement_20'),
]
