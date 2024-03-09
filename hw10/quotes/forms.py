from django.forms import ModelForm, CharField, TextInput, DateField
from .models import Tag, Author


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
                          widget=TextInput() )

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