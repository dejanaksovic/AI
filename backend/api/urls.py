from django.urls import path
from . import views

urlpatterns = [
   path('', views.always_success, name = 'success'),
   path('test/', views.test, name = 'test'),
]