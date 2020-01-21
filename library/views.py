from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from basic_auth.views import BaseView
from library.forms import BookForm
from library.models import Book, Author, Publisher


class BooksListView(BaseView):
    template_name = 'book_list.html'

    def get(self, request, *args, **kwargs):
        context = {
            'books': Book.objects.all().order_by('-publish_date'),
        }
        return render(request, self.template_name, context)


class BooksAddView(BaseView):
    template_name = 'books_add.html'

    def get(self, request, *args, **kwargs):
        context = {
            'authors': Author.objects.all(),
            'publishers': Publisher.objects.all(),
        }
        return render(request, self.template_name, context)

    def post(self,request, *args, **kwargs):
        author_id = request.POST.get('author_id')
        publisher_id = request.POST.get('publisher_id')

        form = BookForm(request.POST, author_id=author_id, publisher_id=publisher_id)

        if form.is_valid():
            print("form is valid")
            data = form.cleaned_data
            Book.objects.create(**data)

        return HttpResponseRedirect(reverse('books_list'))