from django.urls import path
from . import views

urlpatterns = [
    path('blogs/', views.blog_list_create),
    path('blogs/<int:pk>/', views.blog_detail),
]
