from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('legos/', views.legos_index, name='index'),
    path('legos/<int:lego_id>/', views.legos_detail, name='detail'),
]