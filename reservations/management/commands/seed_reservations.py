import random
from datetime import timedelta
from django.core.management.base import BaseCommand
from django.utils import timezone
from django_seed import Seed
from reservations import models as reservations_models
from users import models as users_models
from rooms import models as rooms_models


class Command(BaseCommand):

    help = "This command creates reservations"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            type=int,
            default=1,
            help="How many reservations do you want to create",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()

        users = users_models.User.objects.all()
        rooms = rooms_models.Room.objects.all()

        seeder.add_entity(
            reservations_models.Reservation,
            number,
            {
                "status": lambda x: random.choice(["pending", "confirmed", "canceled"]),
                "check_in": lambda x: timezone.now(),
                "check_out": lambda x: timezone.now()
                + timedelta(days=random.randint(3, 25)),
                "guest": lambda x: random.choice(users),
                "room": lambda x: random.choice(rooms),
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} reservations created!"))
