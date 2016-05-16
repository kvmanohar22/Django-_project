# Create your views here.
#HttpResponse is object
from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says Hello World! <a href='/rango/about/'>About</a>")
#each view exists as series of individual functions
#each view takes in atleast one arguement - a HttpResponse object which lies in
#the django.http module
#each view must return a HttpResponse object
#for a client to access your view you must map a url to the view
def about(request):
    return HttpResponse("Rango says: Here is the about page. <a href='/rango/'>Back</a>")
