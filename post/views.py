from django.shortcuts import render, redirect
from django.http import Http404

# Create your views here.
from .models import Author
from .forms import AuthorForm, BookForm, BookFormSet

def author_add(request):
    if request.method == 'POST':
        author_form = AuthorForm(request.POST)

        if author_form.is_valid():
            created_author = author_form.save(commit=False)
            formset = BookFormSet(request.POST, instance=created_author)

            if formset.is_valid():
                created_author.save()
                formset.save()
                return redirect(created_author)
    else:
        author_form = AuthorForm()
        formset = BookFormSet()

    return render(request, 'post/author_add.html',
                {'author_form':author_form, 'formset':formset })


def author_list(request):
    try:
        author_list = Author.objects.prefetch_related('book_set').all()
    except Author.DoesNotExist:
        raise Http404

    return render(request, 'post/author_list.html', {'author_list':author_list})


def author_detail(request, id):
    try:
        author = Author.objects.prefetch_related('book_set').get(id=id)
    except Author.DoesNotExist:
        raise Http404

    return render(request, 'post/author_detail.html', {'author':author})


def author_update(request, id):

    try:
        author = Author.objects.prefetch_related('book_set').get(id=id)
    except Author.DoesNotExist:
        raise Http404

    if request.method == 'POST':
        author_form = AuthorForm(request.POST, instance=author)

        if author_form.is_valid():
            created_author = author_form.save(commit=False)
            formset = BookFormSet(request.POST, instance=created_author)

            if formset.is_valid():
                created_author.save()
                formset.save()
                return redirect(author)
    else:
        author_form = AuthorForm(instance=author)
        formset = BookFormSet(instance=author)

    return render(request, 'post/author_add.html',
                {'author_form':author_form, 'formset':formset })
