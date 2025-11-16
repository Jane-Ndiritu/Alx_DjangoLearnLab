from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()

    def __str__(self):
        return self.name
class Book(models.Model):
     title = models.Cherfield(max_length=200)
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books'        
        related-name='books'
    )
    def __str__(self):
        return f"{self.title} by {self.author.name}"
    class Library(models.Model):
        name = models.CharField(max_length=100)
        books = models.ManyToManyField(
            Book,
            related_name='libraries'
        )
        def __str__(self):
            return self.name
        class Librarian(models.Model):
            name = models.CharField(max_length=100)
            library = models.OneToOneField(
                Library,
                on_delete=models.CASCADE,
                related_name='librarian'
            )
            def __str__(self):
                return f"{self.name} - {self.library.name}"
            