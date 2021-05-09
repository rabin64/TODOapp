from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="list"),
    path('updatetask/<str:pk>/', views.UpdateTask, name="updatetask"),
    path('delete/<str:pk>/', views.deleteTask, name="delete"),
]