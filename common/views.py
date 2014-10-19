from django.shortcuts import render

from common.models import SearchForm

def homepage(request):
    form = SearchForm()
    return render(request, 'homepage.html', {'form' : form})

