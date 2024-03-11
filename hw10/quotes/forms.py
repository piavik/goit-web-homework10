from django.forms import (
    ModelForm, 
    CharField, 
    TextInput,
    DateField, 
    DateInput,
    ModelChoiceField, 
    ModelMultipleChoiceField, 
    SelectMultiple
)
from .models import Tag, Author, Quote


authors = [ author.fullname for author in Author.objects.all() ]

class TagForm(ModelForm):

    name = CharField(min_length=3, 
                     max_length=25, 
                     required=True, 
                     widget=TextInput())
    
    class Meta:
        model = Tag
        fields = ['name']


class AuthorForm(ModelForm):

    fullname = CharField(min_length=5, 
                         max_length=50, 
                         required=True, 
                         widget=TextInput() )

    born_date = DateField(required=False,
                          widget=DateInput(attrs={'type': "date"}))

    born_location = CharField(min_length=5,
                              max_length=100, 
                              required=False,
                              widget=TextInput() )

    description = CharField(min_length=10, 
                           max_length=150, 
                           required=True,
                           widget=TextInput() )

    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']

class QuoteForm(ModelForm):

    quote = CharField(min_length=3, 
                     required=True, 
                     widget=TextInput() )
    author = ModelChoiceField(queryset=Author.objects.all())
    tags = ModelMultipleChoiceField(queryset=Tag.objects.all(), widget=SelectMultiple(attrs={'size':'10'}))

    class Meta:
        model = Quote
        fields = ['quote', 'author', 'tags']
