from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import TagForm
from .models import Quote, Tag


# Create your views here.
def main(request):
    quotes = Quote.objects.all()
    # quotes = Quote.objects.filter(user=request.user).all() if request.user.is_authenticated else []
    return render(request, 'quotes/index.html', {"quotes": quotes})

@login_required
def delete_quote(request, quote_id):
    Quote.objects.get(pk=quote_id, user=request.user).delete()
    return redirect(to='quotes:main')

# @login_required
def tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotes:main')
        else:
            return render(request, 'quotes/tag.html', {'form': form})

    return render(request, 'quotes/tag.html', {'form': TagForm()})


# def author(request, note_id):
#     author = get_object_or_404(Note, pk=author_id)
#     return render(request, 'quotes/author.html', {"author": author})