from django.shortcuts import render
from django.http import HttpResponse
from website.forms import ContactForm
from django.contrib import messages

def index_view(request):
    return render(request, "website/index.html")

def about_view(request):
    return render(request, "website/about.html")

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        request.POST._mutable = True
        request.POST['name'] = 'Anonymous'
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "your ticket submited")
        else:
            messages.add_message(request, messages.ERROR, "your ticket did not submited")
    form = ContactForm()
    return render(request, "website/contact.html", {"form":form})


