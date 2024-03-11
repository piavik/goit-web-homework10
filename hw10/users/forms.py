from django.forms import CharField, TextInput, PasswordInput, EmailInput
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    username = CharField(max_length=100,
                         required=True,
                         widget=TextInput())
    
    email    = CharField(max_length=100,
                         required=True,
                         widget=EmailInput())

    password1 = CharField(max_length=50,
                          required=True,
                          widget=PasswordInput())
                          
    password2 = CharField(max_length=50,
                          required=True,
                          widget=PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        

class LoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ['username', 'password']


class Avatar(AuthenticationForm):

    class Meta:
        model = User
        fields = ['username', 'password']