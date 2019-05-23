from random import randint
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

def root(request):
    return HttpResponseRedirect('home')

def home_page(request):
    return render(request, 'index.html', {
        'name': 'Betty Maker'
    })   

def portfolio(request):
    image_urls = []
    for i in range(5):
        random_number = randint(0,100)
        image_urls.append("https://picsum.photos/400/600/?image={}".format(random_number))

    context = {'gallery_images': image_urls}
    response = render(request, 'gallery.html', context)
    return HttpResponse(response)

def about_me(request):
    context = {
        'skills': ['dancing', 'singing'], 'interests': ['coffee', 'swimming']
    }
    response = render(request, 'about_me.html', context)
    return HttpResponse(response)

def favourites(request):
    context = {'fave_links': ['cnn.com']}
    response = render(request, 'fave_links.html', context)
    return HttpResponse(response)
