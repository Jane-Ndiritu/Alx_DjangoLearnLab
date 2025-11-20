from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden
from .models import UserProfile, Book, BorrowRecord
from .models import Library
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import permission_required

# Custom decorator to check if user has Admin role
def admin_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        try:
            if request.user.profile.role != 'Admin':
                return HttpResponseForbidden("You don't have permission to access this page.")
        except UserProfile.DoesNotExist:
            return HttpResponseForbidden("You don't have permission to access this page.")
        return view_func(request, *args, **kwargs)
    return wrapper

# Admin dashboard view
@login_required
@admin_required
def admin_dashboard(request):
    # Get statistics for the admin dashboard
    total_users = User.objects.count()
    total_librarians = UserProfile.objects.filter(role='Librarian').count()
    total_members = UserProfile.objects.filter(role='Member').count()
    total_books = Book.objects.count()
    total_libraries = Library.objects.count()
    borrowed_books = BorrowRecord.objects.filter(is_returned=False).count()
    
    # Recent users for display
    recent_users = User.objects.all().order_by('-date_joined')[:5]
    
    context = {
        'total_users': total_users,
        'total_librarians': total_librarians,
        'total_members': total_members,
        'total_books': total_books,
        'total_libraries': total_libraries,
        'borrowed_books': borrowed_books,
        'recent_users': recent_users,
        'active_libraries': total_libraries,  # Assuming all are active
        'total_branches': total_libraries,    # Same as libraries for simplicity
        'last_backup': '2024-01-15 14:30:00', # Example date
    }
    return render(request, 'admin_view.html', context)

# User management view for admins
@login_required
@admin_required
def manage_users(request):
    users = User.objects.all().select_related('profile')
    context = {
        'users': users
    }
    return render(request, 'manage_users.html', context)

# View to change user roles
@login_required
@admin_required
def change_user_role(request, user_id):
    if request.method == 'POST':
        try:
            user = User.objects.get(id=user_id)
            new_role = request.POST.get('role')
            if new_role in ['Admin', 'Librarian', 'Member']:
                user.profile.role = new_role
                user.profile.save()
                # Add success message
                return redirect('manage_users')
        except User.DoesNotExist:
            pass
    return redirect('manage_users')

# User registration view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Automatically create UserProfile with default role 'Member'
            UserProfile.objects.create(user=user, role='Member')
            login(request, user)
            return redirect('book-list')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form}) 

def is_admin(user):
    try:
        return user.profile.role == 'Admin'
    except UserProfile.DoesNotExist:
        return False 
    
def is_member(user):
    try:
        return user.profile.role == 'Member'
    except UserProfile.DoesNotExist:
        return False 
    
def is_librarian(user):
    try:
        return user.profile.role == 'Librarian'
    except UserProfile.DoesNotExist:
        return False 
    
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')


@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')


def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


class LibraryListView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
   
