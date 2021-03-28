from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, LoginPage, Registerpage
from django.contrib.auth.views import  LogoutView
from django.contrib.auth import views as auth_views

urlpatterns =[
    path('',TaskList.as_view(),name='tasks'),
    path('login/',LoginPage.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page= 'login'), name= 'logout'),
    path('register/', Registerpage.as_view(), name='register'),
    path('tasks/<int:pk>', TaskDetail.as_view(), name='task'),
    path('task-create', TaskCreate.as_view(), name= 'task-create'),
    path('task-update/<int:pk>', TaskUpdate.as_view(), name= 'task-update'),
    path('task-delete/<int:pk>', TaskDelete.as_view(), name= 'task-delete'),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name= 'password_reset'),
    path('password_reset_sent/',auth_views.PasswordResetDoneView.as_view(template_name= 'password_reset_sent.html'), name= 'password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name= 'password_reset_confirm.html'), name= 'password_reset_confirm'),
    path('password_reset/complete/',auth_views.PasswordResetCompleteView.as_view(template_name= 'password_reset_complete.html'), name= 'password_reset_complete'),
]