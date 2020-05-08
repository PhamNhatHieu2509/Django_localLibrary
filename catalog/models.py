from django.db import models
from django.urls import reverse
import uuid #Required for unique book instances
# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=200, help_text='Enter a book genre')
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    #book can only have one author, but authors can have multiple books(Onetomany)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000)
    #ManyToMany: genre can contain many books. Books can cover many genres.
    genre = models.ManyToManyField(Genre)
    def __str__(self):
        """String for representing the Model object."""
        return self.title
    

class Author(models.Model):
    """Model representing an author."""
    name = models.CharField(max_length=100)
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name

