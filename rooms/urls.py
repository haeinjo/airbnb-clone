from django.urls import path
from . import views as rooms_views


urlpatterns = [
    path("", rooms_views.all_rooms),
]

