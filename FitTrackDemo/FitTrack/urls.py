from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('calorie/', views.calorie, name='calorie'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('addweight/', views.add_weight, name='add_weight'),
    path('weight_log_delete/<int:weight_id>', views.weight_log_delete, name='weight_log_delete'),
    path('food/list', views.food_list_view, name='food_list'),
    path('food_add_view/', views.food_add_view, name='food_add_view'),
    path('daydate', views.daydate, name='daydate'),
    path('food/foodlog', views.food_log_view, name='food_log_view'),
    path('food/foodlog/delete/<int:food_id>', views.food_log_delete, name='food_log_delete'),
    path('calculate_bmr/', views.calculate_bmr, name='calculate_bmr'),
    path('bmr_log_delete/<int:bmr_id>', views.bmr_log_delete, name='bmr_log_delete'),
   
]