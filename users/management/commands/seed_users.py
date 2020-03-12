from django.core.management.base import BaseCommand
from django_seed import Seed
from users import models as users_models


class Command(BaseCommand):

    help = "This command creates users"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            type=int,
            default=1,
            help="How many users do you want to create?",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        seeder.add_entity(
            users_models.User, int(number), {"is_staff": False, "is_superuser": False}
        )
        seeder.execute()

        self.stdout.write(self.style.SUCCESS(f"{number} users created!"))
