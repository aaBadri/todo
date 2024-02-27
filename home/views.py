from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse("home page")
    person = {"name": "ali", "age": 28}
    return render(request, "home.html", person)
