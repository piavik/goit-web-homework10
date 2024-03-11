from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .forms import TagForm, AuthorForm, QuoteForm
from .models import Quote, Tag, Author


# Create your views here.
def main(request, page=1):
    quotes = Quote.objects.all()
    pages = 10
    paginator = Paginator(quotes, pages)
    quotes_page = paginator.page(page)
    return render(request, 'quotes/index.html', context={"quotes": quotes_page, "page": page})

@login_required
def add_tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotes:main')
        else:
            return render(request, 'quotes/add_tag.html', {'form': form})
    return render(request, 'quotes/add_tag.html', {'form': TagForm()})

def tag_detail(request, tag_id, page=1):
    quotes = Quote.objects.filter(tags=tag_id)
    pages = 10
    paginator = Paginator(quotes, pages)
    quotes_with_tags_page = paginator.page(page)
    return render(request, 'quotes/index.html', context={"quotes": quotes_with_tags_page, "page": page})

@login_required
def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotes:main')
        else:
            return render(request, 'quotes/add_quote.html', context={'form': form})
            
    return render(request, 'quotes/add_quote.html', context={'form': QuoteForm()})      

def author_detail(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(request, 'quotes/author.html', context={"author": author})

@login_required
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotes:main')
        else:
            return render(request, 'quotes/add_author.html', context={'form': form})
            
    return render(request, 'quotes/add_author.html', context={'form': AuthorForm()})            
