from django import forms

from library.models import Author, Publisher


class BookForm(forms.Form):
    name = forms.CharField(max_length=50)
    publish_date = forms.DateField(required=False)

    def __init__(self, *args, **kwargs):
        self.author_id = kwargs.pop('author_id')
        self.publisher_id = kwargs.pop('publisher_id')

        super(BookForm, self).__init__(*args, **kwargs)


    def clean(self):
        cleaned_data = super(BookForm, self).clean()
        print(cleaned_data)

        cleaned_data['author'] = Author.objects.get(id=self.author_id)
        cleaned_data['publisher'] = Publisher.objects.get(id=self.publisher_id)

        return cleaned_data