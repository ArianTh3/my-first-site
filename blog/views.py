from django.shortcuts import render, get_object_or_404
from blog.models import blog_Post
from django.utils import timezone

# Create your views here.

def blog_view(request):
    posts = blog_Post.objects.filter(published_date__lte=timezone.now(), status=1)
    context = {'posts': posts}
    return render(request, "blog/blog-home.html",context)

def blog_single(request, pid):
    post = blog_Post.objects.get(published_date__lte=timezone.now(), status=1, pk=pid)
    post.counted_views += 1
    post.save()
  
    nextpost = blog_Post.objects.filter(id__gt=post.id).order_by('id').first()
    prevpost = blog_Post.objects.filter(id__lt=post.id).order_by('-id').first()
    
    
    context = {'post':post, 'nextpost': nextpost, 'prevpost': prevpost} 
    return render(request, "blog/blog-single.html", context)