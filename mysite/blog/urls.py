from django.urls import path

from . import views

urlpatterns = [
    path('randomnumber', views.models_list),
    path('asas', views.post_list),
]