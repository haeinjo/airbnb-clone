import math
from django.shortcuts import render
from django.core.paginator import Paginator
from . import models as rooms_models


def all_rooms(request):
    page = request.GET.get("page")
    room_list = rooms_models.Room.objects.all()
    paginator = Paginator(room_list, 10)
    rooms = paginator.get_page(page)

    return render(request, "rooms/home.html", {"page": rooms})
