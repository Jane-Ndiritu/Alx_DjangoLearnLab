# Create a Book instance
book = Book(title="1984", 
author="George Orwell", publication_year=1949)

# Save it to the database
book.save()

# Verify it was created
print(Book.objects.all())