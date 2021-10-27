from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path('', views.login, name='login'),
    path('register', views.register, name='register'),
    path('reg/', views.reg, name='reg'),
    path('student_load/', views.student_load, name='student_load'),
    path('confirm/', views.confirm, name='confirm'),
    path('home/', views.home, name='home'),
    path('log_ver/', views.log_ver, name='log_ver'),
    path('log_admin/', views.log_admin, name='log_admin'),
    path('adminlog/', views.adminlog, name='adminlog'),
    path('verify/', views.verify, name='verify'),
    path('adminhome/', views.adminhome, name='adminhome'),
]
