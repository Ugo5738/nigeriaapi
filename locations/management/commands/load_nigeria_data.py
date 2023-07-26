import json

from django.core.management.base import BaseCommand

from locations.models import Location


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('locations.json') as f:
            data = json.load(f)
            for state, cities in data.items():
                for city, coordinates in cities.items():
                    Location.objects.create(state=state, city=city, latitude=coordinates[0], longitude=coordinates[1])
