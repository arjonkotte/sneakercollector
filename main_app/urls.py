from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('sneakers/', views.sneakers_index, name='index'),
    path('sneakers/<int:sneaker_id>/', views.sneaker_details, name='details'),
    path('sneakers/create/', views.SneakerCreate.as_view(), name='sneakers_create'),
    path('sneakers/<int:pk>/update/',
         views.SneakerUpdate.as_view(), name='sneakers_update'),
    path('sneakers/<int:pk>/delete/',
         views.SneakerDelete.as_view(), name='sneakers_delete'),
    path('sneakers/<int:sneaker_id>/add_photo/',
         views.add_photo, name='add_photo'),
]
