from django.contrib import admin
from . models import Genre, Book, BookInstance, Author, Language

# Register your models here.
admin.site.register(Genre)

class BookInline(admin.TabularInline):
    model = Book

# admin.site.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BookInline]
admin.site.register(Author, AuthorAdmin)

#admin.site.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {'fields': ('book', 'imprint', 'id')}),
        ('Availability', {'fields':('status', 'due_back', 'borrower')}),
    )    
admin.site.register(BookInstance, BookInstanceAdmin)

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    
#admin.site.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]
admin.site.register(Book, BookAdmin)

admin.site.register(Language)