from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Print messsage to console'
    
    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Hello from the Dark Web!'))