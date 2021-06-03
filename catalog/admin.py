from django.contrib import admin
from .models import Author, Book, Genre, BookInstance, Language

#admin.site.register(Book)
#admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Language)
#admin.site.register(BookInstance)

class BookInline(admin.TabularInline):
  model = Book
  extra = 0

# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
  list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
  fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
  inlines = [BookInline]

# Register the admin calss with the associated model
admin.site.register(Author, AuthorAdmin)

class BookInstanceInline(admin.TabularInline):
  model = BookInstance
  extra = 0

# Register the Admin calsses for Book using the @admin decorator which does the same thing as the 'admin.site.register()' syntax
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
  list_display = ('title', 'author', 'display_genre')
  inlines = [BookInstanceInline]


# Register the Admin classes for BookInstance with the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
  list_display = ('book', 'status', 'borrower', 'due_back', 'id')
  list_filter = ('status', 'due_back')
  fieldsets = (
    (None, {
      'fields': ('book', 'imprint', 'id')
    }),
    ('Availability', {
      'fields': ('status', 'due_back', 'borrower')
    }),
  )
