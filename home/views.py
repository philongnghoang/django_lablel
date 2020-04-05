from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import RegistrationForm,ButtonClick,NameForm
from django.contrib.auth import authenticate, login
import random
def index(request):
    return render(request,'pages/home.html')
# Create your views here.
def register(request):
    form = RegistrationForm()
    if request.method=='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/home/long')
    return render(request,'pages/register.html',{'form':form})
def button(request):
    i = random.randrange(1,5)
    print(request.user)
    form = ButtonClick()
    if request.method == 'POST':
        form= ButtonClick(request.POST)
        if form.is_valid():
            val = form.cleaned_data.get('btn')
    return render(request,'pages/home.html',{'form':form,'link':'/static/media/'+str(i)+'.jpg','username':request.user})
def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            val = form.cleaned_data['your_name']
    else:
        form = NameForm()

    return render(request, 'pages/home.html', {'form': form})