from django.shortcuts import render, redirect
from  django.http import HttpResponse
from .models import Hostel

# Create your views here.
def homepage(request) :
    # return HttpResponse("Hi Hello How Are You ??????")
    if request.method == "POST" :
        h_name= request.POST["h_name"]
        h_add= request.POST["h_add"]
        h_obj = Hostel.objects.create(name = h_name, add = h_add)
        return redirect(homepage)
    else :
        return render(request, template_name = "home.html")
    

def show(request) :
    all_h = Hostel.objects.all()
    data = {"hs" : all_h}
    return render(request, template_name = "show.html", context = data)
    