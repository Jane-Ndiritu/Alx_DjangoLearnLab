from bookshelf.models import Book

# Update directly in the database without retrieving the object first
Book.objects.filter(title="1984").update(title="Nineteen Eighty-Four")

# ✅ Verify the update using the *new* title
updated_book = Book.objects.get(title="Nineteen Eighty-Four")
print(f"Book details: {updated_book}")
