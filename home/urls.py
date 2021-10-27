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
<<<<<<< HEAD
    path('adddish/', views.add_dish, name='adddish'),
    path('add_item/', views.add_item, name='additem'),
    path('viewdish/', views.viewdish, name='viewdish'),
    path('dish_load/', views.dish_load, name='dish_load'),
    path('delete_dish/', views.delete_dish, name='delete_dish'),
    path('edit/', views.edit_dish, name='edit_dish'),
    path('edit_item/', views.edit_item, name='edit_item'),
    path('view_waste/', views.view_waste, name='view_waste'),
    path('add_waste/', views.add_waste, name='add_waste'),
    path('load_waste/', views.load_waste, name='load_waste'),
    path('dishs/', views.dishs, name='dishs'),
    path('show_dish/', views.show_dish, name='show_dish'),
    path('post_review/', views.post_review, name='post_review'),
    path('show_review/', views.show_review, name='show_review'),
    path('raise_comp/', views.raise_comp, name='raise_comp'),
    path('raise_camp/', views.raise_camp, name='raise_camp'),
    path('add_comp/', views.add_comp, name='add_comp'),
    path('add_camp/', views.add_camp, name='add_camp'),
    path('comp/', views.comp, name='comp'),
    path('view_comp/', views.view_comp, name='view_comp'),
    path('comp_detail/', views.comp_detail, name='comp_detail'),
    path('admin_comp_detail/', views.admin_comp_detail, name='admin_comp_detail'),
    path('show_comp/', views.show_comp, name='show_comp'),
    path('student_nav/', views.student_nav, name='student_nav'),
    path('admin_nav/', views.admin_nav, name='admin_nav'),
    path('all_camps/', views.all_camps, name='all_camps'),
    path('all_camps_admin/', views.all_camps_admin, name='all_camps_admin'),
    path('vote_page/', views.vote_page, name='vote_page'),
    path('vote/', views.vote, name='vote'),
    path('vote_page_admin/', views.vote_page_admin, name='vote_page_admin'),
    path('vote_admin/', views.vote_admin, name='vote_admin'),
    path('logout_stu/', views.logout_stu, name='logout_stu'),
    path('logout_admin/', views.logout_admin, name='logout_admin'),
    path('stu_waste/', views.stu_waste, name='stu_waste'),
    path('admin_view_comp/', views.admin_view_comp, name='admin_view_comp'),
    path('admin_comp/', views.admin_comp, name='admin_comp'),
=======
>>>>>>> 4a97713f1a1fe005134fd2c29ff509416f5334d3
]
