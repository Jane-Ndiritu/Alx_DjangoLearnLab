from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views.register import list_books, LibraryDetailView, register, admin_dashboard, manage_users, change_user_role
from .views import list_books 

urlpatterns = [
    path('books/', list_books, name='book-list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    
    # Admin routes
    path('admin/dashboard/', admin_dashboard, name='admin_dashboard'),
    path('admin/manage-users/', manage_users, name='manage_users'),
    path('admin/change-role/<int:user_id>/', change_user_role, name='change_user_role'),
]