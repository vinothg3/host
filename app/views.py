from django.shortcuts import render

# Create your views here.

def host(request):
    return render(request,'host.html')