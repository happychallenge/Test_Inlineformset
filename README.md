# Test_Inlineformset
모델을 정의한다. 모델은 Author 와 Book 이 1:M 의 관계를 갖는다.

### models.py
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
       
### forms.py
폼은 특별한 것이 없고, 기존 모델 폼을 사용하고, inlineformset_factory 함수를 사용하여 Author, Book의 관계를 표현한다.
from django import forms
from django.forms import inlineformset_factory


from .models import Author, Book

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', ]

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['author', 'name', 'pages', 'price']

BookFormSet = inlineformset_factory(Author, Book, form=BookForm, extra=2)

### urls.py

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.author_list, name='author_list'),
    url(r'^(?P<id>\d+)/$', views.author_detail, name='author_detail'),
    url(r'^update/(?P<id>\d+)/$', views.author_update, name='author_update'),
    url(r'^add/$', views.author_add, name='author_add'),
]
