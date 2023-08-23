from django import template
from blog.models import blog_Post

from blog.models import Category

from blog.models import Comment


register = template.Library() 

@register.inclusion_tag("blog/blog-popular-post.html")
def latestpost(args=3):
    posts = blog_Post.objects.filter(status=1).order_by('-published_date')[:args]
    return {"posts":posts}



@register.inclusion_tag("blog/blog-category.html")
def postcategories():
    posts = blog_Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name] = posts.filter(category=name).count()
    return {"categories":cat_dict}


@register.inclusion_tag("website/latestposts.html")
def index_latestpost(args=6):
    posts = blog_Post.objects.filter(status=1).order_by('-published_date')[:args]
    return {"posts":posts}

@register.simple_tag(name='comments_count')
def func(pid):
    comment = Comment.objects.filter(posts=pid,approved=True).count()
    
    return comment