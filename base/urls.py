from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('person/', views.person, name='person'),
]
