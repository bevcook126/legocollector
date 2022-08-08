from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('legos/', views.legos_index, name='index'),
    path('legos/<int:lego_id>/', views.legos_detail, name='detail'),
    path('legos/create/', views.LegoCreate.as_view(), name='legos_create'),
    path('legos/<int:pk>/update/', views.LegoUpdate.as_view(), name='legos_update'),
    path('legos/<int:pk>/delete/', views.LegoDelete.as_view(), name='legos_delete'),
]