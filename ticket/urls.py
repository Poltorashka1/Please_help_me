from django.urls import path
from ticket import views

app_name = 'ticket'


urlpatterns = [
    path('', views.get_all_ticket, name='all_ticket'),
    path('detail/<int:pk>/', views.get_ticket_info, name='detail'),
    path('buy_ticket/<int:pk>/<str:action>/', views.buy_ticket, name='buy_ticket')
]
