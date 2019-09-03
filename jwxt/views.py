from django.shortcuts import render
from django.http import HttpResponse
from .models import ArticlePost
# Create your views here.
def helloworld(request):
    return HttpResponse("hello world")

def show_course(request):
    return render(request, "courses_table.html")

def post_index(request):

    articles = ArticlePost.objects.all()
    content = {'articles': articles}

    return render(request, "blog/index.html", content)