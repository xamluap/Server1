from django.shortcuts import render

def index(request):
    return render(request, 'home/index.html')

'''
def about(request):
    return render(request, 'home/about.html')

def blog(request):
    return render(request, 'home/blog.html')

def contact(request):
    return render(request, 'home/contact.html')

def generic(request):
    return render(request, 'home/eneric.html')

def index(request):
    return render(request, 'home/index.html')

def produced_index(request):
    return render(request, 'home/produced_index.html')

def services(request):
    return render(request, 'home/services.html')

def single(request):
    return render(request, 'home/isingle.html')

def styles(request):
    return render(request, 'home/styles.html')''' 