from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    # return HttpResponse("<h1>Hello world</h1>")
    return render(request, 'home.html', {})


def contact_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Contact page</h1>")
    my_context = {
        'my_text': 'This is a contact page',
        'my_number': 123,
    }
    return render(request, 'contact.html', {})

def about_view(request, *args, **kwargs):
    # return HttpResponse("<h1>About page</h1>")
    my_context = {
        'my_text': 'This is about page',
        'my_number': 123,
        'my_list': [12, 124, 'String', True]
    }
    return render(request, 'about.html', my_context)




