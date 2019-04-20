from django.contrib import admin
from .models import Customer, Address


class AddressInLine(admin.StackedInline):
    model = Address
    extra = 0


#Change display for the customer model
class CutomerAdmin(admin.ModelAdmin):
    list_display = ('First_Name', 'Last_Name','Phone' )

    inlines = [AddressInLine]


# Register Customer Model in Admin
admin.site.register(Customer, CutomerAdmin)
