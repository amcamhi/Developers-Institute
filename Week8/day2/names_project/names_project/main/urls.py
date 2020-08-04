from django.urls import path
from . import views

urlpatterns = [
    path('', views.people, name='people'),
    path('<str:id_num>/', views.people_id, name='id_page')

]
