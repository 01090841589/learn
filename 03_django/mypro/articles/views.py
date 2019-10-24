from django.shortcuts import render
from .models import Articles
from .forms import ArticleForm
def index(request):
    return render(request, 'articles/index.html')

def new(request):
    form = ArticleForm()    
    context = {
        'form': form,
    }
    return render(request, 'articles/new.html', context)

# Create your views here.
