from bookshelf.models import Book

# Delete the book directly without retrieving it first
deleted_count, _ = Book.objects.filter(title="Nineteen Eighty-Four").delete()
print(f"Deleted {deleted_count} book(s)")

# Verify deletion by checking all remaining books
remaining_books = Book.objects.all()
print(f"Remaining books: {list(remaining_books)}")
