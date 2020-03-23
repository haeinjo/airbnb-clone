from django.views.generic import ListView, DetailView
from django.http import Http404
from django.shortcuts import render
from django_countries import countries
from . import models


class HomeView(ListView):

    """ HomeView Definition """

    model = models.Room
    paginate_by = 10
    context_object_name = "rooms"


class RoomDetail(DetailView):

    """ RoomDetail Definition """

    model = models.Room


def search(request):
    city = str.capitalize(request.GET.get("city", "Anywhere"))
    country = request.GET.get("country", "KR")
    room_type = int(request.GET.get("room_type", 0))
    price = int(request.GET.get("price", 0))
    guests = int(request.GET.get("guests", 0))
    bedrooms = int(request.GET.get("bedrooms", 0))
    beds = int(request.GET.get("beds", 0))
    baths = int(request.GET.get("baths", 0))
    s_facilities = request.GET.getlist("facilities")
    s_amenities = request.GET.getlist("amenities")
    superhost = bool(request.GET.get("superhost", False))
    instant_book = bool(request.GET.get("instant_book", False))

    form = {
        "city": city,
        "s_country": country,
        "s_room_type": room_type,
        "s_amenities": s_amenities,
        "s_facilities": s_facilities,
        "price": price,
        "guests": guests,
        "bedrooms": bedrooms,
        "beds": beds,
        "baths": baths,
        "superhost": superhost,
        "instant_book": instant_book,
    }

    room_types = models.RoomType.objects.all()
    amenities = models.Amenity.objects.all()
    facilities = models.Facility.objects.all()

    choices = {
        "countries": countries,
        "room_types": room_types,
        "amenities": amenities,
        "facilities": facilities,
    }

    filter_args = {}

    if city != "Anywhere":
        filter_args["city__startswith"] = city

    if room_type != 0:
        filter_args["room_type__pk"] = room_type

    if price != 0:
        filter_args["price__lte"] = price

    if guests != 0:
        filter_args["guests__gte"] = guests

    if bedrooms != 0:
        filter_args["bedrooms_gte"] = bedrooms

    if beds != 0:
        filter_args["beds__gte"] = beds

    if baths != 0:
        filter_args["baths__gte"] = baths

    if instant_book is True:
        filter_args["instant_book"] = True

    if superhost is True:
        filter_args["host__superhost"] = True

    if len(s_amenities):
        for s_amenity in s_amenities:
            filter_args["amenities"] = int(s_amenity)

    if len(s_facilities):
        for s_facility in s_facilities:
            filter_args["facilities"] = int(s_facility)

    filter_args["country"] = country

    rooms = models.Room.objects.filter(**filter_args)

    return render(request, "rooms/search.html", {**form, **choices, "rooms": rooms})


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
