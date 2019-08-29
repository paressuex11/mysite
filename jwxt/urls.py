from django.urls import path


from .views import show_course, helloworld, post_index




urlpatterns = [
    path('course_table/', show_course),
    path('hello/', helloworld),
    path('blog/', post_index),
   

]


