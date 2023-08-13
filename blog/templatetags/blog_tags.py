from django import template
from blog.models import blog_Post


register = template.Library() 

@register.inclusion_tag("blog/blog-popular-post.html")
def latestpost(args=3):
    posts = blog_Post.objects.filter(status=1).order_by('published_date')[:args]
    return {"posts":posts}