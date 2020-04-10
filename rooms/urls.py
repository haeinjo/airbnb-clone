from django.urls import path
from . import views as rooms_views

app_name = "rooms"

urlpatterns = [
    path("<int:pk>/", rooms_views.RoomDetail.as_view(), name="detail"),
    path("<int:pk>/edit/", rooms_views.EditRoomView.as_view(), name="edit"),
    path("search/", rooms_views.SearchView.as_view(), name="search"),
]
