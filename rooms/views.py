import math
from django.shortcuts import render
from . import models as rooms_models


def all_rooms(request):
    page = request.GET.get("page", 1)
    page = int(page or 1)
    page_size = 10
    page_limit = page_size * page
    offset = page_limit - page_size

    all_rooms = rooms_models.Room.objects.all()[offset:page_limit]
    page_size = rooms_models.Room.objects.count() / page_size
    page_size = math.ceil(page_size)

    return render(
        request,
        "rooms/home.html",
        context={"all_rooms": all_rooms, "page": page, "page_size": page_size},
    )
