from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ArticlePost
from .forms import ArticlePostForm
from django.contrib.auth.models import User

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

def create_article(request):
    if (request.method == "POST"):
        article_post_form = ArticlePostForm(data = request.POST)
        if article_post_form.is_valid():
            # 保存数据，但暂时不提交到数据库中
            new_article = article_post_form.save(commit=False)
            # 指定数据库中 id=1 的用户为作者
            # 如果你进行过删除数据表的操作，可能会找不到id=1的用户
            # 此时请重新创建用户，并传入此用户的id
            new_article.author = User.objects.get(id=1)
            # 将新文章保存到数据库中
            new_article.save()
            # 完成后返回到文章列表
            return redirect("jwxt:blog")
        # 如果数据不合法，返回错误信息
        else:
            return HttpResponse("表单内容有误，请重新填写。")
    # 如果用户请求获取数据
    else:
        # 创建表单类实例
        article_post_form = ArticlePostForm()
        # 赋值上下文
        context = { 'article_post_form': article_post_form }
        # 返回模板
        return render(request, 'blog/create.html', context)