from django.contrib import admin

from books.models import *

# Register your models here.

admin.site.register(books)
admin.site.register(takenbooks)