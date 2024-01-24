from django.urls import path
from . import views

urlpatterns = [
   path('', views.always_success, name = 'success'),
   path('position/', views.get_position, name = 'position'),
   path('algorithm', views.algorithm, name='algorithm')
]