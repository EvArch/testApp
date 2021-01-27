from django.shortcuts import render
from django.http import HttpResponse
from .models import Users
from .forms import LoginForm
# Create your views here.

def adduser(request):
    if request.method == 'POST':
        data = Users(username=request.POST.get("username"),password=request.POST.get("password"),email=request.POST.get("email"))
        data.save()

    return render(request, 'pages/index.html', {'form': LoginForm()})
