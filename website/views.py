from pprint import pprint

from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from website.forms import ArticleForm, LoginForm
from website.models import Article


# Create your views here.

def index(request):

    return render(request, "website/home/index.html")
def articles(request):
    articles = Article.objects.all()
    context = {
        "articles": articles
    }
    return render(request, "website/article/articles.html", context)


def get_article(request, id):
    article = Article.objects.get(id=id)
    return render(request, "website/article/show.html", {'article': article})

def create_article(request):

    if not request.user.is_authenticated:
        return HttpResponseRedirect('/')
    article = Article()
    if request.method == "POST":
        form = ArticleForm(request.POST)

        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return HttpResponseRedirect('/')

    form= ArticleForm()
    return render(request,"website/article/create.html",{'form': form})
def edit_article(request,id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/')
    article = Article.objects.get(id=id)
    if request.method == "POST":
        form = ArticleForm(request.POST,instance=article)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    form= ArticleForm(instance=article)
    return render(request,"website/article/create.html",{'form': form})

def delete_article(request,id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/')

    article = Article.objects.get(id=id)
    article.delete()
    return HttpResponseRedirect('/')

def register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username =form.cleaned_data.get('username')
            if User.objects.filter(username=username).exists() :
                return render(request, "website/registration/login.html",
                              {'form': form, "formName": "Register", "error": "invalid name"})

            password = form.cleaned_data.get('password')
            user = User.objects.create_user(username=username,password=password)
            user.save()
            login(request,user)
            return HttpResponseRedirect('/login')
        return render(request,"website/registration/login.html",{'form':form,"formName":"Register","error":"form invalid"})

    return render(request,"website/registration/login.html",{'form':form,"formName":"Register"})
def login_user(request):

    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if(user is  None):
                return HttpResponseRedirect('/register')
            login(request,user)
            return HttpResponseRedirect('/articles')
        return render(request,"website/registration/login.html",{'form':form,"formName":"Register","error":"form invalid"})

    return render(request,"website/registration/login.html",{'form':form,"formName":"Login"})

def logout_truc(request):
    logout(request)
    return HttpResponseRedirect('/')