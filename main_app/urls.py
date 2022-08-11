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
    path('legos/<int:lego_id>/add_minifig/', views.add_minifig, name='add_minifig'),
    path('legos/<int:lego_id>/assoc_collection/<int:collection_id>/', views.assoc_collection, name='assoc_collection'),
    path('legos/<int:lego_id>/unassoc_collection/<int:collection_id>/', views.unassoc_collection, name='unassoc_collection'),
    path('legos/<int:lego_id>/add_photo/', views.add_photo, name='add_photo'),
    path('collections/', views.CollectionList.as_view(), name='collections_index'),
    path('collections/<int:pk>/', views.CollectionDetail.as_view(), name='collections_detail'),
    path('collections/create/', views.CollectionCreate.as_view(), name='collections_create'),
    path('collections/<int:pk>/update/', views.CollectionUpdate.as_view(), name='collections_update'),
    path('collections/<int:pk>/delete/', views.CollectionDelete.as_view(), name='collections_delete'),
]