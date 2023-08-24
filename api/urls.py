from django.urls import path
from . import views

urlpatterns = [
    path('populate/', views.populate, name='populate'),
    path('planets/', views.get_planets, name='get_planets'),
    path('planet/', views.create_planet, name='create_planet'),
    path('planet/<int:pk>/', views.update_planet, name='update_planet'),
    path('planet/<int:pk>/delete/', views.delete_planet, name='delete_planet'),
]