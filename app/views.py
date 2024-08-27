from django.shortcuts import render
from django.http import HttpResponse
def conditions(request):
    d={'a':100,'b':200}
    return render(request,'conditions.html',d)

# Create your views here.
