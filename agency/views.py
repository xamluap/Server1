from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'agency/index.html',{})

def index1(request):
    return render(request,'agency/index1.html',{})
