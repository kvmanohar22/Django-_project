# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says Hello World! <a href='/rango/about'>About</a>")
#request is an object of HttpRequest
#each view must return an HttpResponse object

def about(request):
    return HttpResponse("Rango says this is the about page!! <a href='/rango/'>Back</a>")
