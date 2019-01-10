from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    book_code = models.CharField(max_length=10)
    book_title = models.CharField(max_length=500)
    author_name = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
