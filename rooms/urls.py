from django.urls import path
from . import views as rooms_views

app_name = "rooms"

urlpatterns = [
    path("<int:pk>/", rooms_views.RoomDetail.as_view(), name="detail"),
    path("search/", rooms_views.search, name="search"),
]
