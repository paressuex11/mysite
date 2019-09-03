from django.urls import path


from .views import show_course, helloworld, post_index, get_detail, create_article


app_name = 'jwxt'

urlpatterns = [
    path('course_table/', show_course),
    path('hello/', helloworld),
    path('blog/', post_index, name = "blog"),
    path('blog/detail/<int:id>', get_detail, name = "detail"),
    path('blog/create', create_article, name = "create"),

]


