from django.urls import path
from . import views

urlpatterns = [
    path('api/membership/', views.membership_create, name='membership_create'),
]
