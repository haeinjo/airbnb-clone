from django.urls import path
from . import views as rooms_views

app_name = "rooms"

urlpatterns = [
    path("<int:pk>/", rooms_views.RoomDetail.as_view(), name="detail"),
    path("<int:pk>/edit/", rooms_views.EditRoomView.as_view(), name="edit"),
    path("<int:pk>/photos", rooms_views.RoomPhotosView.as_view(), name="photos"),
    path(
        "<int:room_pk>/pothos/<int:photo_pk>/delete/",
        rooms_views.delete_photo,
        name="delete-photo",
    ),
    path(
        "<int:room_pk>/photos/<int:photo_pk>/edit",
        rooms_views.EditPhotoView.as_view(),
        name="edit-photo",
    ),
    path("search/", rooms_views.SearchView.as_view(), name="search"),
]
