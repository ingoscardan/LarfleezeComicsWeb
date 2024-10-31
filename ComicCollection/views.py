from django.http import HttpResponse
from django.conf import settings

# Create your views here.
def index(request):
     key = settings.COMICVINE_API_KEY
     return HttpResponse("Your Comic-Vine Api Key is " + key)