from tkinter.font import names

from django.urls import path
from .views import login_view, logout_view, register_user, custom_admin_dashboard, api_stats

urlpatterns = [
    path('', login_view, name='login'),  # Root URL directs to login page
    path('dashboard/', custom_admin_dashboard, name='custom_admin_dashboard'),
    path('register/', register_user, name='register'),
    path('api/stats/', api_stats, name='api_stats'),
    path('logout/', logout_view, name='logout')
]
