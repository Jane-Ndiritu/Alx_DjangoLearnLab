#!/usr/bin/env python
"""
Relationship Query Samples Script
This script demonstrates various relationship queries for the library system.
"""

import os
import django
import sys

# Setup Django environment
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def setup_sample_data():
    """Create sample data for testing queries"""
    print("Setting up sample data...")
    
    # Clear existing data
    Librarian.objects.all().delete()
    Library.objects.all().delete()
    Book.objects.all().delete()
    Author.objects.all().delete()
    
    # Create authors
    author1 = Author.objects.create(name="George Orwell")
    author2 = Author.objects.create(name="J.K. Rowling")
    author3 = Author.objects.create(name="Agatha Christie")
    
    # Create books
    book1 = Book.objects.create(title="1984", author=author1)
    book2 = Book.objects.create(title="Animal Farm", author=author1)
    book3 = Book.objects.create(title="Harry Potter and the Philosopher's Stone", author=author2)
    book4 = Book.objects.create(title="Harry Potter and the Chamber of Secrets", author=author2)
    book5 = Book.objects.create(title="Murder on the Orient Express", author=author3)
    book6 = Book.objects.create(title="And Then There Were None", author=author3)
    
    # Create libraries
    library1 = Library.objects.create(name="City Central Library")
    library2 = Library.objects.create(name="University Library")
    
    # Add books to libraries
    library1.books.add(book1, book2, book3, book5)  # Mixed collection
    library2.books.add(book3, book4, book6)  # Focus on fantasy and mystery
    
    # Create librarians
    librarian1 = Librarian.objects.create(name="Alice Johnson", library=library1)
    librarian2 = Librarian.objects.create(name="Bob Smith", library=library2)
    
    print("Sample data created successfully!\n")
    return author1, author2, library1, library2

def query_all_books_by_specific_author(author_name):
    """
    Query 1: Get all books by a specific author
    Demonstrates ForeignKey reverse relationship using related_name='books'
    """
    print("=" * 60)
    print("QUERY 1: All books by a specific author")
    print("=" * 60)
    
    try:
        # Method 1: Using filter
        print(f"\nMethod 1 - Using filter (Books by {author_name}):")
        books_method1 = Book.objects.filter(author__name=author_name)
        for book in books_method1:
            print(f"  - {book.title}")
        
        # Method 2: Using reverse relationship (more efficient)
        print(f"\nMethod 2 - Using reverse relationship (Books by {author_name}):")
        author = Author.objects.get(name=author_name)
        books_method2 = author.books.all()  # Using related_name='books'
        for book in books_method2:
            print(f"  - {book.title}")
            
        return books_method2
        
    except Author.DoesNotExist:
        print(f"Author '{author_name}' not found.")
        return []

def list_all_books_in_library(library_name):
    """
    Query 2: List all books in a specific library
    Demonstrates ManyToManyField relationship
    """
    print("\n" + "=" * 60)
    print("QUERY 2: All books in a specific library")
    print("=" * 60)
    
    try:
        # Method 1: Using filter
        print(f"\nMethod 1 - Using filter (Books in {library_name}):")
        library = Library.objects.get(name=library_name)
        books_method1 = library.books.all()  # Using ManyToMany relationship
        for book in books_method1:
            print(f"  - {book.title} by {book.author.name}")
        
        # Method 2: Using through model (if you need more complex queries)
        print(f"\nMethod 2 - Count and details (Books in {library_name}):")
        book_count = library.books.count()
        print(f"  Total books in library: {book_count}")
        for book in library.books.select_related('author').all():
            print(f"  - '{book.title}' by {book.author.name}")
            
        return books_method1
        
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")
        return []

def retrieve_librarian_for_library(library_name):
    """
    Query 3: Retrieve the librarian for a specific library
    Demonstrates OneToOneField relationship
    """
    print("\n" + "=" * 60)
    print("QUERY 3: Librarian for a specific library")
    print("=" * 60)
    
    try:
        # Method 1: Using direct lookup
        print(f"\nMethod 1 - Direct lookup (Librarian for {library_name}):")
        library = Library.objects.get(name=library_name)
        librarian = library.librarian  # Using OneToOne reverse relationship
        print(f"  Librarian: {librarian.name}")
        print(f"  Manages: {librarian.library.name}")
        
        # Method 2: Using filter
        print(f"\nMethod 2 - Using filter (Librarian for {library_name}):")
        librarian_method2 = Librarian.objects.get(library__name=library_name)
        print(f"  Librarian: {librarian_method2.name}")
        
        return librarian
        
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")
        return None
    except Librarian.DoesNotExist:
        print(f"No librarian found for library '{library_name}'.")
        return None

def additional_demonstration_queries():
    """Additional useful relationship queries"""
    print("\n" + "=" * 60)
    print("ADDITIONAL DEMONSTRATION QUERIES")
    print("=" * 60)
    
    # Query: Libraries that have books by a specific author
    print("\n1. Libraries that have books by George Orwell:")
    libraries_with_orwell = Library.objects.filter(books__author__name="George Orwell").distinct()
    for library in libraries_with_orwell:
        print(f"  - {library.name}")
    
    # Query: Authors whose books are in a specific library
    print("\n2. Authors with books in City Central Library:")
    authors_in_central = Author.objects.filter(books__libraries__name="City Central Library").distinct()
    for author in authors_in_central:
        print(f"  - {author.name}")
    
    # Query: Books count per author
    print("\n3. Book count per author:")
    from django.db.models import Count
    authors_with_counts = Author.objects.annotate(book_count=Count('books'))
    for author in authors_with_counts:
        print(f"  - {author.name}: {author.book_count} books")

def main():
    """Main function to run all query demonstrations"""
    print("RELATIONSHIP QUERY SAMPLES")
    print("=" * 60)
    
    # Setup sample data
    author1, author2, library1, library2 = setup_sample_data()
    
    # Run the required queries
    query_all_books_by_specific_author("George Orwell")
    list_all_books_in_library("City Central Library")
    retrieve_librarian_for_library("City Central Library")
    
    # Additional demonstrations
    additional_demonstration_queries()
    
    print("\n" + "=" * 60)
    print("ALL QUERIES COMPLETED SUCCESSFULLY!")
    print("=" * 60)

if __name__ == "__main__":
    main()