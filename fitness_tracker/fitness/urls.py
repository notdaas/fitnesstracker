from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('log_activity/', views.log_activity, name='log_activity'),
    path('set_goal/', views.set_goal, name='set_goal'),
    path('profile/', views.profile, name='profile'),
]
