import secrets
import string

from django.conf import settings
from django.contrib.auth.models import User
from django.core.management import BaseCommand


def generate_random_password(length: int = 15) -> str:
    alphabet = string.ascii_letters + string.digits
    password = "".join(secrets.choice(alphabet) for _ in range(length))
    return password


class Command(BaseCommand):
    def handle(self, *args, **options):
        if User.objects.count() == 0:
            for user in settings.ADMINS:
                username = user["username"]
                email = user["email"]
                password = generate_random_password()
                print(
                    f"Creating account for {username} ({email}) with password: {password}"
                )
                admin = User.objects.create_superuser(
                    email=email, username=username, password=password
                )
                admin.is_active = True
                admin.is_admin = True
                admin.save()
        else:
            print("Admin accounts can only be initialized if no Accounts exist")
