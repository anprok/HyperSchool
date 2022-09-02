from django.db import models


class Book(models.Model):
    author = models.CharField(max_length=200)
    class Meta:
        app_label = 'books'
        ordering = ['-author']