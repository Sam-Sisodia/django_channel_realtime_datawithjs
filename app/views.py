from django.shortcuts import render

# Create your views here.



def home(request):
    return render(request, "index.html")

def realdata(request):
    pass
    return render(request, "realdata.html")