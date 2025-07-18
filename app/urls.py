from django.urls import path
from . import views


urlpatterns = [
    path('', views.index_view, name='index'),
    path('car_detail/<int:car_id>/', views.car_detail_view, name='detail'),
    path('car_create/', views.car_create_view, name='car_create')
]
