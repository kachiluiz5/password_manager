

from django.urls import path
from . import views

app_name = 'manager'

urlpatterns = [
    path('password-list/', views.password_list, name='password_list'),  # Add this line
    path('', views.generate_password, name='generate_password'),
    path('generate-password/', views.generate_password, name='generate_password'),
    path('update-password/<int:password_id>/', views.update_password, name='update_password'),
    path('delete-password/<int:password_id>/', views.delete_password, name='delete_password'),
]
