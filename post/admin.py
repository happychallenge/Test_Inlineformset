from django.contrib import admin
from .models import Author, Book

# # Register your models here.
# @admin.register(Book)
# class BookAdmin(admin.ModelAdmin):
#     class Meta:
#         model = Book
#     list_display = ['author', 'name', 'pages', 'price']

class BookInline(admin.TabularInline):
    model = Book

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    class Meta:
        model = Author
    list_display = ['name', 'created_at']
    inlines = [ BookInline ]
