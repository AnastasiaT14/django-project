from django.db import models

class Book(models.Model):
    book_title = models.CharField(max_length=20)
    book_author = models.CharField(max_length=20)
    book_release_date = models.DateField()
    description = models.CharField(max_length=150)

