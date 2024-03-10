from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import TagForm, AuthorForm
from .models import Quote, Tag, Author


# Create your views here.
def main(request):
    quotes = Quote.objects.all()
    # authors = Author.objects.all()
    return render(request, 'quotes/index.html', context={"quotes": quotes}) #, "authors": authors})

def main_paginated(request):
    ...


def tag(request):
    tags = Tag.objects.all()
    return render(request, 'quotes/index.html', context={"tags": tags})

def tag_detail(request):
    tags = Tag.objects.all()
    return render(request, 'quotes/index.html', context={"tags": tags})

def search_by_tag(request):
    ...

def quote_detail(request):
    ...

@login_required
def add_quote(request, quote_id):
    Quote.objects.get(pk=quote_id, user=request.user).delete()
    return redirect(to='quotes:main')

# def author(request):
#     authors = Author.objects.all()
#     quotes = Quote.objects.all()
#     return render(request, 'quotes/author.html', context={"authors": authors})

def author_detail(request):
    author = get_object_or_404(Author, pk=author_id)
    # quotes = Quote.objects.filter(author=author)
    return render(request, 'quotes/author.html', context={"author": author})

@login_required
def add_author(request):
    # tags = Tag.objects.all()
    tags = Tag.objects.filter(user=request.user).all()

    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            new_author = form.save()
            return redirect(to='quotes:main')
        else:
            return render(request, 'quotes/author.html', context={"tags": tags, 'form': form})

