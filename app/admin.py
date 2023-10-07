from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Customer
from .models import Product
# Register your models here.
# class CustomUserAdmin(UserAdmin):
#     list_display = ('uname','uemail')
    #   search_fields = ('uname','email')


admin.site.register(Customer)
admin.site.register(Product)