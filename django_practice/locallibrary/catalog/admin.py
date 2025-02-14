from django.contrib import admin
from .models import Genre, Book, Author, Language, BookInstance

# Register your models here.
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'id ', 'due_back', 'status')
    list_filter = ('status', 'due_back')
    search_fields = ('title')
    
class BookInline(admin.TabularInline):
    model = Book
    extra = 1
    
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name','first_name', 'date_of_birth', 'date_of_death')
    search_fields = ('last_name', 'first_name')
    inlines = [BookInline]

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(BookInstance)
