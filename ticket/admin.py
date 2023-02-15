from django.contrib import admin
from ticket import models


# Register your models here.
# @admin.register(models.Passenger)
# class PassengerAdmin(admin.ModelAdmin):
#     list_display = ('name', 'email')
#     ordering = ('name',)


@admin.register(models.Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('departure_city', 'city_of_arrival')
    ordering = ('-time_of_arrival',)


@admin.register(models.City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)
