from django.contrib import admin

from library_catalog.models import Book, Author


class BookAdmin(admin.ModelAdmin):
    model = Book

    list_display = ('title', 'time_create')
    list_filter = ['title', 'time_create']
    search_fields = ['title']
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Book, BookAdmin)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'time_create')
    list_filter = ['last_name', 'first_name']
    search_fields = ['last_name', 'first_name']

    prepopulated_fields = {"slug": ('first_name', 'last_name')}


admin.site.register(Author, AuthorAdmin)
