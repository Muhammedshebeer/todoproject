from django.shortcuts import render,redirect,get_list_or_404
from.models import *

# Create your views here.

def home(request):
    show=Todo.objects.all()
    return render(request, 'main.html',{'show':show})
def todo(request):
    if request.method == 'POST':
        titles = request.POST['title']
        discription = request.POST['discription']
        abc=Todo(Titles=titles,Description=discription)
        abc.save()
        return redirect('/home')
    
def delt(request,id):
    a=Todo.objects.get(id=id)    
    a.delete()
    return redirect('/home')

def update(request):
    edit=get_list_or_404(Todo,id=id)
    if request.method == 'POST':
        newtitle=request.POST['title']
        newdiscription=request.POST['discription']
        edit.Titles=newtitle
        edit.Description=newdiscription
        edit.save()
        return redirect('/home')
    return render(request, 'main.html',{'edit':edit})
        
        