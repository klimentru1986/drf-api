import time

from django.core.management.base import BaseCommand
from django.db.utils import OperationalError


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write('Waiting for db')
        db_con = False

        while db_con is False:
            try:
                self.check(databases=["default"])
                db_con = True
            except OperationalError:
                self.stdout.write('Db coonection timeout')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Db connected!'))
