from django.shortcuts import render, redirect
from .models import Article
from django.core.exceptions import ValidationError
from IPython import embed

def index(request):
    articles = Article.objects.order_by('-pk')
    # print(articles)
    # print(type(articles))
    context = {'articles': articles}
    return render(request, 'articles/index.html', context)

def new(request):
    # embed
    return render(request, 'articles/new.html')

    
def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        article = Article(title=title, content=content, image=image)
        article.full_clean()
        article.save()
        # embed()
        return redirect('articles:detail', article.pk)
    else:
        return render(request, 'articles/create.html')

    # try:
    #     title = request.POST.get('title')
    #     content = request.POST.get('content')
    #     article = Article(title=title, content=content)
    #     article.full_clean()
    # except ValidationError:
    #     raise ValidationError('Your Error Message')
    # else:
    #     article.save()
    #     return redirect('articles:detail', article.pk)
    #1. 첫번째 방법
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    #2. 두번째 방법
    # article = Article(title=title, content=content)
    # article.save()
    # return render(request, 'articles/index.html')

    #3. 세번째 방법
    # Article.objects.create(title=title, content=content)
    # return redirect(f'/articles/{article.pk}/')


def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    comments = article.comments.all()
    context = {'article': article, 'comments':comments}
    return render(request, 'articles/detail.html', context)

def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    article.delete()
    return redirect('articles:index')


def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {'article': article}
    return render(request,'articles/edit.html', context)

def update(request, pk):
    # embed
    article = Article.objects.get(pk=pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    context = {
        'article': article,
        
        
        
        }

    return redirect('articles:detail', article.pk)

def comments_create(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        content = request.POST.get('content')
        comment = Comment(article=article, content=content)
        comment.save()
        return redirect('articles:detail')
    else:
        return redirect('article:detail', article.pk)
def comments_delete(request, article_pk, comment_pk):
    if request.method == 'POST':
        comment = Comment.objects.get(pk=comment_pk)
        comment.delete()
    return redirect('articles:detail', article_pk)

def comments_update(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.method == 'POST':
        comment.content = request.POST.get('content')
        comment.save()
        return redirect('articles:detail')
    else:
        context = {'comment':comment}
        return render(request, 'articles/comment_update.html')
