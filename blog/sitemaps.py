from django.contrib.sitemaps import Sitemap
from blog.models import blog_Post

class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return blog_Post.objects.filter(status=True)

    def lastmod(self, obj):
        return obj.published_date
    