from django.contrib import admin
from .models import blog_Post, Category
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.




class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'   
    list_display = ('title' , 'author','counted_views','status','published_date','created_date')
    list_filter = ('status', 'author')
    search_fields = ['title','content']
    summernote_fields = ('content',)

admin.site.register(Category)
admin.site.register(blog_Post, PostAdmin)