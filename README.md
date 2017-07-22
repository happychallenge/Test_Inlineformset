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

    BookFormSet = inlineformset_factory(Author, Book, form=BookForm, extra=2)  # **가장 중요한 부문**

### urls.py
URL 도 달라지는 것은 없음

   from django.conf.urls import url
    from . import views

    urlpatterns = [
        url(r'^$', views.author_list, name='author_list'),
        url(r'^(?P<id>\d+)/$', views.author_detail, name='author_detail'),
        url(r'^update/(?P<id>\d+)/$', views.author_update, name='author_update'),
        url(r'^add/$', views.author_add, name='author_add'),
    ]

### Views.py

    from django.shortcuts import render, redirect
    from django.http import Http404

    # Create your views here.
    from .models import Author
    from .forms import AuthorForm, BookForm, BookFormSet

    def author_add(request):
        if request.method == 'POST':
            author_form = AuthorForm(request.POST) # Author 정보 form 에 저장

            if author_form.is_valid():
                created_author = author_form.save(commit=False) # Author 정보를 Commit 전까지 저장
                formset = BookFormSet(request.POST, instance=created_author) # Book List 정보를 form 에 저장 

                if formset.is_valid():
                    created_author.save()  # Author 정보를 DB 에 저장
                    formset.save()         # Book List 를 DB 에 저장
                    return redirect(created_author)
        else:
            author_form = AuthorForm()     # Author  Form
            formset = BookFormSet()        # Book List Form

        return render(request, 'post/author_add.html',
                    {'author_form':author_form, 'formset':formset })
                    
### post/author_add.html ==> Horizontal Table 형태로 보여줌
   <h2>Author Add</h2>

    <form action="" method="POST">
    {% csrf_token %}
    <div>
        {{ author_form.as_table }}
    </div>

    <div>
        <table id="formset" class="form">
        {{ formset.management_form }}
        {% for form in formset.forms %}
            {% if forloop.first %}
                <thead>
                    <tr>
                        {% for field in form.visible_fields %}
                        <th>{{ field.label|capfirst }}</th>
                        {% endfor %}
                    </tr>
                </thead>
            {% endif %}
                <tr>
                {% for field in form.visible_fields %}
                    <td>
                    {# Include the hidden fields in the form #}
                    {% if forloop.first %}
                        {% for hidden in form.hidden_fields %}
                            {{ hidden }}
                        {% endfor %}
                    {% endif %}
                    {{ field.errors.as_ul }}
                    {{ field }}
                    </td>
                {% endfor %}
                </tr>
        {% endfor %}
        </table>
    </div>
    <input type="submit" value='Confirm'>
    </form>
    
### post/author_add_list.html  ==> 아래로 Stack type 으로 
    <h2>Author Add</h2>

    <form action="" method="POST">
    {% csrf_token %}
    <div>
        {{ author_form.as_table }}
    </div>

    <div>
        <table id="formset" class="form">
            {{ formset.as_table }}
        </table>
    </div>
    <input type="submit" value='Confirm'>
    </form>    
