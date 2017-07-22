from django.db import models
from django.shortcuts import reverse

class Author(models.Model):
    """docstring for Authro"""
    """ 설명 """
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post:author_detail', args=[self.id])


class Book(models.Model):
    """docstring for Book"""
    """ 설명 """
    author = models.ForeignKey(Author, null=True, blank=True)
    name = models.CharField(max_length=30)
    pages = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    


