from django.urls import path

import ComicCollection.views
from .views import PublisherListView, comic_collection_landing

app_name = "ComicCollection"
urlpatterns = [
    path("", comic_collection_landing, name="publisher-landing"),
    path("Publishers/", PublisherListView.as_view(), name="publisher-list"),
]