from django.urls import path, include
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('', blog_view, name='index'),
    path('blog-single.html/<int:pid>', blog_single, name='single')
] 