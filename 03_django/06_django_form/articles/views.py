from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from IPython import embed
from django.views.decorators.http import require_POST

def index(request):
    #1. session 정보에서 visits_num 이라는 키로 접근해 값을 가져옴.
    #해당하는 키가 없으면 0을 가져옴
    visits_num = request.session.get('visits_num', 0)
    request.session['visits_num'] = visits_num + 1

    request.session.modified = True
    articles = Article.objects.all()
    context = {
        'articles': articles,
        'visits_num': visits_num,
    }
    return render(request, 'articles/index.html', context)


@login_required
def create(request):
    """
    Form Class
    1. 모델에 대한 정보를 알지 못해서 유효성 검사 이휴에 clean_data를 통해 데이터 정제 후 DB에 실제 저장하는 로직 필요

    Model Form
    이미 Model에 대한 정보를 알고 있기 때문에 어떤 모델에 레코드를 넣어야 하는지 알고 있음.
    """
    if request.method == 'POST':
        # fomr 인스턴스를 생성하고 요청에 의한 데이터로 채운다.
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
                # title = form.cleaned_data.get('title')
                # content = form.cleaned_data.get('content')
                # article = Article(title=title, content=content)
                # article.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()
    context = {
        'form':form,
    }
    return render(request, 'articles/form.html', context)

def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    article_form = ArticleForm()
    comment_form = CommentForm()

    comments = article.comments.all
    context = {
        'article':article,
        'comment_form':comment_form,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)

@require_POST
def delete(request, article_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=article_pk)
        article.delete()
    return redirect('articles:index')

def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article.title = form.cleaned_data.get('title')
            article.content = form.cleaned_data.get('content')
            article.save()
            return redirect('articles:detail', article_pk)
    else:
        form = ArticleForm(initial=article.__dict__)
    context = {'form':form, 'article':article}
    return render(request, 'articles/form.html', context)

@require_POST
def comments_create(request, article_pk):
    if request.user.is_authenticated:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article_id = article_pk
    # article = get_object_or_404(Article, pk=article_pk)
    # comment = comment_form.save(commit=False)
    # comment.article = article
        comment.save()
    return redirect('articles:detail', article_pk)

@require_POST
def comments_delete(request, article_pk, comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        comment.delete()
    return redirect('articles:detail', article_pk)
