from django.urls import path

from robot import views


app_name = 'robot'

urlpatterns = [
    path('', views.home, name='home'),
    path('robot/', views.robot, name='robot'),
    path('error/', views.error, name='error'),
]
