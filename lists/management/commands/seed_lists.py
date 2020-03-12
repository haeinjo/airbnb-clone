import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from lists import models as lists_models
from users import models as users_models
from rooms import models as rooms_models


class Command(BaseCommand):

    help = "This command creates lists"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", type=int, default=1, help="How many do you want to create lists"
        )

    def handle(self, *args, **options):
        number = options.get("number")

        seeder = Seed.seeder()
        users = users_models.User.objects.all()
        rooms = rooms_models.Room.objects.all()

        seeder.add_entity(
            lists_models.List, number, {"user": lambda x: random.choice(users)}
        )

        created_lists = seeder.execute()
        cleaned_lists = flatten(list(created_lists.values()))

        for pk in cleaned_lists:
            this_list = lists_models.List.objects.get(pk=pk)

            for room in rooms:
                flag = random.randint(0, 4)
                if flag == 1:
                    this_list.rooms.add(room)

        self.stdout.write(self.style.SUCCESS(f"{number} lists created!"))
