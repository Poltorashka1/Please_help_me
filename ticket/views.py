from django.shortcuts import render, redirect
from ticket import models


# Create your views here.
def get_all_ticket(request):
    """Отображение всех билетов"""
    all_ticket = models.Ticket.objects.all()
    return render(request, 'all_ticket.html', {"all_ticket": all_ticket})


def get_ticket_info(request, pk):
    """Информация о каждом билете"""
    ticket = models.Ticket.objects.filter(id=pk)
    return render(request, 'ticket_info.html', {'ticket': ticket})


def buy_ticket(request, pk, action):
    """Покупка билета(Появляется в профиле)"""
    tik = models.Ticket.objects.get(id=pk)
    tik.passenger.add(request.user)
    return redirect('users:user_profile')
