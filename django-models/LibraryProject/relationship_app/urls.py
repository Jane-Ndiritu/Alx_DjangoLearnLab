from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import list_books, register, admin_dashboard

urlpatterns = [
    path('books/', list_books, name='book-list'),
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    
    # Admin-only route - this is explicitly checked in the view
    path('admin/dashboard/', admin_dashboard, name='admin_dashboard'),
]