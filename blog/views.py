from django.shortcuts import render, get_object_or_404
from blog.models import blog_Post, Comment
from django.utils import timezone
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from blog.forms import CommentForm
from django.contrib import messages
from django.urls import reverse
from django.shortcuts import HttpResponseRedirect

# Create your views here.

def blog_view(request, **kwargs):
    posts = blog_Post.objects.filter(published_date__lte=timezone.now(), status=1)
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username=kwargs['author_username'])
    if kwargs.get('tag_name') != None:
         posts = posts.filter(tags__name__in=[kwargs['tag_name']])
    posts = Paginator(posts, 3)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
         posts = posts.get_page(1)
    context = {'posts': posts}
    return render(request, "blog/blog-home.html",context)

def blog_single(request, pid):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Your comment has been posted successfully")
        else:
            messages.add_message(request, messages.ERROR, "Your comment could not be posted")
    
    post = blog_Post.objects.get(published_date__lte=timezone.now(), status=1, pk=pid)
    post.counted_views += 1
    post.save()
  
    nextpost = blog_Post.objects.filter(id__gt=post.id, status=1).order_by('id').first()
    prevpost = blog_Post.objects.filter(id__lt=post.id, status=1).order_by('-id').first()
    
    if not post.login_required:
        comments = Comment.objects.filter(posts=post.id, approved=True)
        form = CommentForm()
        context = {'post':post, 'nextpost': nextpost, 'prevpost': prevpost, 'comments': comments, 'form': form} 
        return render(request, "blog/blog-single.html", context)
    else:
        return HttpResponseRedirect(reverse('accounts:login'))


def blog_category(request, cat_name):
     posts = blog_Post.objects.filter(published_date__lte=timezone.now(), status=1)
     posts = posts.filter(category__name=cat_name)
     context = {'posts': posts}
     return render(request, "blog/blog-home.html",context)
 
def blog_search(request):
    posts = blog_Post.objects.filter(published_date__lte=timezone.now(), status=1)
    if request.method == "GET":
        if s := request.GET.get('s'):
            posts = posts.filter(content__contains=s)
    context = {'posts': posts}
    return render(request, "blog/blog-home.html",context)