import csv
import os

from django.conf import settings
from django.core.management.base import BaseCommand
from recipes.models import Ingredient, Tag

DATA_DIR = os.path.join(settings.BASE_DIR, 'data')


class Command(BaseCommand):
    help = 'Create demo data'

    def handle(self, *args, **options):
        # Создание тегов
        Tag.create_default_tags()

        def create_objects_from_csv(file_path, create_func):
            with open(file_path, 'r') as csv_file:
                reader = csv.reader(csv_file)
                for row in reader:
                    create_func(*row)

        def create_ingredient(name, measurement_unit):
            Ingredient.objects.update_or_create(
                name=name, measurement_unit=measurement_unit)

        create_objects_from_csv(
            os.path.join(DATA_DIR, 'ingredients.csv'),
            create_ingredient
        )

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
