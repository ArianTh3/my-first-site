from django.contrib import admin

# Register your models here.
from .models import blog_Post, Category



class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'   
    list_display = ('title' , 'author','counted_views','status','published_date','created_date')
    list_filter = ('status', 'author')
    search_fields = ['title','content']

admin.site.register(Category)
admin.site.register(blog_Post, PostAdmin)