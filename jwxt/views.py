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
def get_detail(request, id):
    import markdown
    article = ArticlePost.objects.get(id = id)

    article.body = markdown.markdown(article.body,
        extensions=[
        # 包含 缩写、表格等常用扩展
        'markdown.extensions.extra',
        # 语法高亮扩展
        'markdown.extensions.codehilite',
        ])

    content = {'article': article}
    return render(request, "blog/detail.html", content)