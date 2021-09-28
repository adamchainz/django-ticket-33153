from django.db import models


class Author(models.Model):
    pass


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
