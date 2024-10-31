from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render

from django.views.generic import ListView

from ComicCollection.models import Publisher


# Create your views here.
def index(request):
     key = settings.COMICVINE_API_KEY
     return HttpResponse("Your Comic-Vine Api Key is " + key)


class PublisherListView(ListView):
    model = Publisher
    template_name = "ComicCollection/publishers_list.html"


def comic_collection_landing(request):
    return render(request, "ComicCollection/landing.html")