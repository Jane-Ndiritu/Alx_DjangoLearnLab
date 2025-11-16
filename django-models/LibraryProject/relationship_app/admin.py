from django.contrib import admin

from django.contrib import admin
from .models import UserProfile, Library, Book, BorrowRecord, Reservation, Fine

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'role', 'phone_number', 'membership_id', 'is_active']
    list_filter = ['role', 'is_active']
    search_fields = ['user__username', 'user__email', 'membership_id']

@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'phone_number', 'email']
    search_fields = ['name', 'address']

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'genre', 'status', 'available_copies', 'library']
    list_filter = ['genre', 'status', 'library']
    search_fields = ['title', 'author', 'isbn']

@admin.register(BorrowRecord)
class BorrowRecordAdmin(admin.ModelAdmin):
    list_display = ['book', 'user', 'borrow_date', 'due_date', 'is_returned']
    list_filter = ['is_returned', 'borrow_date']
    search_fields = ['book__title', 'user__username']

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ['book', 'user', 'reservation_date', 'expiration_date', 'is_active']
    list_filter = ['is_active', 'reservation_date']

@admin.register(Fine)
class FineAdmin(admin.ModelAdmin):
    list_display = ['user', 'amount', 'reason', 'issue_date', 'is_paid']
    list_filter = ['is_paid', 'issue_date']
    search_fields = ['user__username']
