import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from rooms import models as rooms_models
from users import models as users_models


class Command(BaseCommand):

    help = "This command creates rooms"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", type=int, default=1, help="How many rooms do you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_users = users_models.User.objects.all()
        all_roomtypes = rooms_models.RoomType.objects.all()
        amenities = rooms_models.Amenity.objects.all()
        facilities = rooms_models.Facility.objects.all()
        rules = rooms_models.HouseRule.objects.all()

        seeder.add_entity(
            rooms_models.Room,
            number,
            {
                "name": lambda x: seeder.faker.address(),
                "host": lambda x: random.choice(all_users),
                "room_type": lambda x: random.choice(all_roomtypes),
                "guest": lambda x: random.randint(1, 20),
                "price": lambda x: random.randint(1, 300),
                "beds": lambda x: random.randint(1, 5),
                "bedrooms": lambda x: random.randint(1, 5),
                "baths": lambda x: random.randint(1, 5),
            },
        )
        created_rooms = seeder.execute()
        cleaned_rooms = flatten(list(created_rooms.values()))

        for pk in cleaned_rooms:
            room = rooms_models.Room.objects.get(pk=pk)
            for i in range(random.randint(3, 14)):
                rooms_models.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    room=room,
                    file=f"room_photos/{random.randint(1, 31)}.webp",
                )

            for a in amenities:
                flag = random.randint(1, 3)
                if flag == 1:
                    room.amenities.add(a)

            for f in facilities:
                flag = random.randint(1, 3)
                if flag == 1:
                    room.facilities.add(f)

            for r in rules:
                flag = random.randint(1, 3)
                if flag == 1:
                    room.house_rules.add(r)

        self.stdout.write(self.style.SUCCESS(f"{number} rooms created!"))
