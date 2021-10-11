from django.urls import path

from . import views

app_name = 'hardware'
urlpatterns = [
    path('', views.index, name = "index"),
]