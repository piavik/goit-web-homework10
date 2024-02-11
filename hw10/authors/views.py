from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import AuthorForm
from .models import Author
# Create your views here.

def main():
    ...
#   return render(request, 'author/author.html', {"tags": tags, 'form': AuthorForm()})

# @login_required
def add_author(request):
    # tags = Tag.objects.all()
    tags = Tag.objects.filter(user=request.user).all()

    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            new_author = form.save()
            return redirect(to='quotes:main')
        else:
            return render(request, 'authors/author.html', {"tags": tags, 'form': form})

  