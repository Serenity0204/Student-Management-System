from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index_view, name='index'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('student_list/', views.student_list_view, name='student_list'),
    path('add_student/', views.add_student_view, name='add_student'),
    path('update_student/<int:pk>/', views.update_student_view, name='update_student'),
    path('delete_student/<int:pk>/', views.delete_student_view, name='delete_student'),
]
