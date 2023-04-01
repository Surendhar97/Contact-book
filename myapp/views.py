from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Yellowpages
def saveinfo(request):
    if request.method == "POST":
        FirstName=request.POST['firstname']
        LastName=request.POST['lastname']
        City=request.POST['city']
        ContactNumber=request.POST['phone']
        add=Yellowpages(FirstName=FirstName,LastName=LastName,City=City,ContactNumber=ContactNumber)
        add.save()
    Data = Yellowpages.objects.all()
    return render(request,"index.html",{'Data':Data})
def index(request):
    Data = Yellowpages.objects.all()
    return render(request,"index.html",{'Data':Data})
def formupdate(request,id):
        if request.method=="POST":
            add=Yellowpages.objects.get(id=id)
            add.FirstName=request.POST["firstname"]
            add.LastName=request.POST["lastname"]
            add.City=request.POST["city"]
            add.ContactNumber=request.POST['phone']
            add.save()
            return redirect("index")
def edit(request,id):
        Data = Yellowpages.objects.get(id=id)
        return render(request,'edit.html',{'Data':Data})
def delete(request,id):
        add = Yellowpages.objects.get(id=id)
        add.delete()
        return redirect('index')
def search(request):
    query=request.GET["query1"]
    Data=Yellowpages.objects.filter(ContactNumber__icontains=query)
    params={'Data':Data}
    return render(request,'search.html',params)