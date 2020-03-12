import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from reviews import models as reviews_models
from rooms import models as rooms_models
from users import models as users_models


class Command(BaseCommand):

    help = "This command creates reviews"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            type=int,
            default=1,
            help="How many do you want to create reviews",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()

        rooms = rooms_models.Room.objects.all()
        users = users_models.User.objects.all()

        # for i in range(number):
        #     reviews_models.Review.objects.create(
        #         review=seeder.faker.sentence(),
        #         accuracy=random.randint(0, 5),
        #         communication=random.randint(0, 5),
        #         cleanliness=random.randint(0, 5),
        #         location=random.randint(0, 5),
        #         check_in=random.randint(0, 5),
        #         value=random.randint(0, 5),
        #         user=random.choice(users),
        #         room=random.choice(rooms),
        #     )

        seeder.add_entity(
            reviews_models.Review,
            number,
            {
                "accuracy": lambda x: random.randint(0, 6),
                "communication": lambda x: random.randint(0, 6),
                "cleanliness": lambda x: random.randint(0, 6),
                "location": lambda x: random.randint(0, 6),
                "check_in": lambda x: random.randint(0, 6),
                "value": lambda x: random.randint(0, 6),
                "user": lambda x: random.choice(users),
                "room": lambda x: random.choice(rooms),
            },
        )
        seeder.execute()

        self.stdout.write(self.style.SUCCESS(f"{number} reviews created!"))
