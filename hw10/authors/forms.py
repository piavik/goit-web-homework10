from django.forms import ModelForm, CharField, TextInput
from .models import Author


class AuthorForm(ModelForm):

    fullname = CharField(min_length=5, 
                         max_length=50, 
                         required=True, 
                         widget=TextInput() )

    born_date = DateTimeField(auto_now_add=False, 
                              required=False,
                              widget=TextInput() )

    born_location = CharField(min_length=5,
                              max_length=100, 
                              required=False,
                              widget=TextInput() )

    description = harField(min_length=10, 
                           max_length=150, 
                           required=True,
                           widget=TextInput() )

    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']

