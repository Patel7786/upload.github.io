from django.urls import path
from .import views

urlpatterns = [
    path('prajjawal',views.home, name = 'home'),
]