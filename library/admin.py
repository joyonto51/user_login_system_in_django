from django.contrib import admin

from library.models import Author, Publisher, Book

models = [Author, Publisher, Book]

admin.site.register(models)