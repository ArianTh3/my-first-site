from django.shortcuts import render, get_object_or_404
from blog.models import blog_Post
from django.utils import timezone
# Create your views here.

def blog_view(request):
    posts = blog_Post.objects.filter(status=1)
    
    return render(request, "blog/blog-home.html", {'posts': posts})

def blog_single(request, pid):
    
    post = get_object_or_404(blog_Post, id=pid)
    
    
    
    posts = blog_Post.objects.filter(published_date__lte=timezone.now())
    
    blog_object=blog_Post.objects.get(id=pid)
    blog_object.blog_views += 1
    blog_object.save()
    
        
    return render(request, "blog/blog-single.html",{'test': post, 'tests': posts} )