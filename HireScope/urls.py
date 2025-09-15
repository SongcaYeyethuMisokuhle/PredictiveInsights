from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('input/', views.candidate_input, name='candidate_input'),
]
