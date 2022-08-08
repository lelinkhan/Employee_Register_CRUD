from django.contrib import admin
from .models import Employee,Position

# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name','emp_code','mobile','position')

@admin.register(Position)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['title']