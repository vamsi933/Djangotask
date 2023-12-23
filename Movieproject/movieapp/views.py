from django.shortcuts import render
from . models import Movies

# Create your views here.
def home(request):
    if request.method =="POST":
        ename = request.POST['name']
        edirector = request.POST['director']
        ebudget = request.POST['budget']
        eheroname = request.POST['heroname']
        eno_of_hits = request.POST['no_of_hits']
        a = Movies(name = ename,director= edirector,budget=ebudget,heroname=eheroname,no_of_hits=eno_of_hits)
        a.save()

    moviename = Movies.objects.all()
    return render(request,'index.html',{'data':moviename})