from django.shortcuts import render, get_object_or_404
from blog.models import blog_Post
from django.utils import timezone
# Create your views here.

def blog_view(request):
    posts = blog_Post.objects.filter(published_date__lte=timezone.now(), status=1)
    context = {'posts': posts}
    return render(request, "blog/blog-home.html",context)

def blog_single(request, pid):
    
    
    blog_object = get_object_or_404(blog_Post, pk=pid)
    blog_object.counted_views += 1
    blog_object.save()
    
    context = {'post':blog_object} 
    return render(request, "blog/blog-single.html", context)