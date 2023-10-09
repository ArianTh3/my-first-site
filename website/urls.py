from django.urls import path, include
from website.views import *

app_name = 'website'

urlpatterns = [
    path('' , coming_soon_view),
    path('', index_view, name='index'),
    path('about', about_view, name='about'),
    path('contact', contact_view, name='contact')
]