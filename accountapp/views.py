from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def hello_world(request):
    return render(request, 'base.html') # template ㅇㅣ름인 base.html을 넣어줘야됨