from django.urls import path
from . import views as rooms_views

app_name = "rooms"

urlpatterns = [
    path("<int:pk>/", rooms_views.room_detail, name="detail"),
]