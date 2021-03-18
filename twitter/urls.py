from django.urls import path
from .views import GetDataView, ListDataView, SingleDataView

app_name = "twitter"

urlpatterns = [
    path('search/', GetDataView.as_view(),
    name="search-view"),
    
    path('list/', ListDataView.as_view(),
    name="list-view"),

    path('single/<id>/', SingleDataView.as_view(),
    name="single-view")
]