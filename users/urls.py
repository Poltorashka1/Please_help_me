from django.urls import path
from users import views

app_name = 'users'

urlpatterns = [
    path('profile/', views.userprofile, name='user_profile'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('admin/', views.admin, name='admin'),
    path('admin/user/', views.admin_user, name='admin_user'),
    path('admin/ticket/', views.admin_ticket, name='admin_ticket'),
    path('admin/user/delete_user/<int:pk>/', views.delete_user, name='delete')
]
