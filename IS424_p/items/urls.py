from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('home', views.list_items, name='list_items'),
    path('<int:item_id>/', views.detail_item, name='detail_item'),
    path('add/', views.add_item, name='add_item'),
    path('<int:item_id>/update/', views.update_item, name='update_item'),
]

