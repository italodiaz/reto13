from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from .forms import AuthorForm

# Create your views here.
def Home(request):
    return render(request, 'libro/index.html', {})

@require_http_methods(["GET", "POST"])
def CreateAuthor(request):
    if request.method == "POST":
        author_form = AuthorForm(request.POST)
        if author_form.is_valid():
            author_form.save()
            return redirect('libro:index')
    else:
        author_form = AuthorForm()

    return render(request, 'libro/create_author.html', {
        'author_form': author_form
    })
