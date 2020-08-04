from django.urls import path
from . import views


urlpatterns = [
    path('', views.info, name='info'),
    path('animal/', views.animal, name='animal'),
    path('family/', views.family, name='family')
]
