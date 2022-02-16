import csv

from django.core.management.base import BaseCommand

from phones.models import Phone
# from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            # TODO: Добавьте сохранение модели
            p = Phone(id=phone.get('id'),
                      name=phone.get('name'),
                      image=phone.get('image'),
                      price=phone.get('price'),
                      release_date=phone.get('release_date'),
                      lte_exist=phone.get('lte_exists'),
                      slug=(phone.get('name')).lower().replace(' ', '-'),
                      )
            p.save()
            # pass
