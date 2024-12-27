from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name='routes'),
    path('admin/', views.getAdmin, name='admin'),
    path('employees/', views.getEmployee, name='employees'), 
    path('employee/<int:pk>/', views.getEmployeeById, name='employee'),
    path('employee/delete/<int:pk>/', views.deleteEmployee, name='delete_employee'),
]
