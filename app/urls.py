from django.urls import path
from . import views


urlpatterns = [
    path('', views.index_view, name='index'),
    path('car_detail/<int:car_id>/', views.car_detail_view, name='detail'),
    path('car_create/', views.car_create_view, name='car_create'),
    path('car_update/<int:car_id>/', views.car_update_view, name='car_update'),
    path('car_delete/<int:car_id>/', views.car_delete_view, name='car_delete'),

    path('car_create_2', views.car_create_2),
    path('user_register/', views.user_register_view, name='register'),
    path('user_login/', views.user_login_view, name='login'),
    path('user_logout/', views.user_logout_view, name='logout')
]
