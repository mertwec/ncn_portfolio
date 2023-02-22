from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from  ncn.settings import ADMIN_USER

class Command(BaseCommand):
    help = 'Creates a superuser.'

    def handle(self, *args, **options):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username=ADMIN_USER["login"],
                password=ADMIN_USER["password"],
            )
        print('Superuser has been created.')
