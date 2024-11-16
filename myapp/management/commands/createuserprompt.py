from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.management.base import BaseCommand
from django.core.validators import validate_email
import getpass

# Create custom command with prompt
class Command(BaseCommand):
    help = 'Create normal user with prompt'

    def handle(self, *args, **kwargs):
        username = input("Enter the Username: ")
        email = input("Enter Email Id: ")
        password = getpass.getpass("Enter the Password: ")
        password_confirm = getpass.getpass("Enter the Password (again): ")

        if password != password_confirm:
            self.stdout.write(self.style.ERROR("Password didn't matched"))
            return

        try:
            validate_email(email)

        except ValidationError:
            self.stdout.write(self.style.ERROR(
                "Error: Enter valid email address."))
            return

        if User.objects.filter(username=username).exists():
            self.stdout.write(self.style.ERROR("Username already exists"))
            return

        if User.objects.filter(email=email).exists():
            self.stdout.write(self.style.ERROR("Email already exist"))
            return

        try:
            User.objects.create_user(
                username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS(
                f'User {username} created successfully'))

        except ValidationError as e:
            self.stdout.write(self.style.ERROR(f'Error: {e.message_dict}'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {str(e)}'))
