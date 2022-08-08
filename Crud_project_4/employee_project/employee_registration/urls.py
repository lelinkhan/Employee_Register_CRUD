from django.urls import path
from . import views

urlpatterns = [
    path('',views.employee_form, name='employee_form'),
    path('list/', views.employee_list, name='list'),
    path('edit/<int:id>',views.employee_form, name='edit'),
    path('delete/<int:id>',views.employee_delete, name='delete'),
]