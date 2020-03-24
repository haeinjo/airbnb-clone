from django.views.generic import ListView, DetailView, View
from django.shortcuts import render
from . import models, forms


class HomeView(ListView):

    """ HomeView Definition """

    model = models.Room
    paginate_by = 10
    context_object_name = "rooms"


class RoomDetail(DetailView):

    """ RoomDetail Definition """

    model = models.Room


def search(request):

    country = request.GET.get("country")
    if country:
        form = forms.SearchForm(request.GET)
        if form.is_valid():
            city = form.cleaned_data.get("city")
            country = form.cleaned_data.get("country")
            room_type = form.cleaned_data.get("room_type")
            price = form.cleaned_data.get("price")
            guests = form.cleaned_data.get("guests")
            bedrooms = form.cleaned_data.get("bedrooms")
            beds = form.cleaned_data.get("beds")
            baths = form.cleaned_data.get("baths")
            instant_book = form.cleaned_data.get("instant_book")
            superhost = form.cleaned_data.get("superhost")
            amenities = form.cleaned_data.get("amenities")
            facilities = form.cleaned_data.get("facilities")

            filter_args = {}

            if city != "Anywhere":
                filter_args["city__startswith"] = city

            filter_args["country"] = country

            if room_type is not None:
                filter_args["room_type"] = room_type

            if price is not None:
                filter_args["price__lte"] = price

            if guests is not None:
                filter_args["guest__gte"] = guests

            if bedrooms is not None:
                filter_args["bedrooms__gte"] = bedrooms

            if beds is not None:
                filter_args["beds_gte"] = beds

            if baths is not None:
                filter_args["baths"] = baths

            if instant_book:
                filter_args["instant_book"] = True

            if superhost:
                filter_args["superhost"] = True

            for amenity in amenities:
                filter_args["amenities"] = amenity

            for facility in facilities:
                filter_args["facilities"] = facility

            rooms = models.Room.objects.filter(**filter_args)
            return render(request, "rooms/search.html", {"form": form, "rooms": rooms})
    else:
        form = forms.SearchForm()

    return render(request, "rooms/search.html", {"form": form})


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
