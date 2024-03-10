from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .forms import TagForm, AuthorForm
from .models import Quote, Tag, Author


# Create your views here.
def main(request, page=1):
    quotes = Quote.objects.all()
    pages = 10
    paginator = Paginator(quotes, pages)
    quotes_page = paginator.page(page)
    return render(request, 'quotes/index.html', context={"quotes": quotes_page, "page": page})

def tag(request):
    tags = Tag.objects.all()
    return render(request, 'quotes/add_tag.html', context={"tags": tags})

def tag_detail(request, tag_id, page=1):
    quotes = Quote.objects.filter(tags=tag_id)
    pages = 10
    paginator = Paginator(quotes, pages)
    quotes_with_tags_page = paginator.page(page)
    return render(request, 'quotes/index.html', context={"quotes": quotes_with_tags_page, "page": page})


def search_by_tag(request):
    ...

@login_required
def add_quote(request, quote_id):
    Quote.objects.get(pk=quote_id, user=request.user).delete()
    return redirect(to='quotes:main')

def author_detail(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
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

