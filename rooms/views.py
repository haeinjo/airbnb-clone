from django.views.generic import ListView
from django.shortcuts import render
from . import models


class HomeView(ListView):

    """ HomeView Definition """

    model = models.Room
    paginate_by = 10
    context_object_name = "rooms"


def room_detail(request, pk):
    return render(request, "rooms/detail.html")


# from django.shortcuts import render, redirect
# from django.core.paginator import Paginator, EmptyPage
# from . import models as rooms_models


# def all_rooms(request):
#     _page = request.GET.get("page", 1)
#     room_list = rooms_models.Room.objects.all()
#     paginator = Paginator(room_list, 10)
#     try:
#         page = paginator.page(_page)
#         return render(request, "rooms/home.html", {"page": page})
#     except EmptyPage:
#         return redirect("/")


# def all_rooms(request):
#     page = request.GET.get("page", 1)
#     page = int(page or 1)
#     page_size = 10
#     limit = page * page_size
#     offset = limit - page_size
#     rooms = rooms_models.Room.objects.all()[offset:limit]
#     page_count = rooms_models.Room.objects.count() / page_size
#     page_count = ceil(page_count)

#     return render(
#         request,
#         "rooms/home.html",
#         {
#             "rooms": rooms,
#             "page": page,
#             "page_count": page_count,
#             "page_range": range(1, page_count + 1),
#         },
#     )


# import math
# from django.shortcuts import render
# from django.core.paginator import Paginator
# from . import models as rooms_models


# def all_rooms(request):
#     page = request.GET.get("page")
#     room_list = rooms_models.Room.objects.all()
#     paginator = Paginator(room_list, 10)
#     rooms = paginator.get_page(page)

#     return render(request, "rooms/home.html", {"page": rooms})
