from django.urls import path
from myapp.views import home,print_message

urlpatterns = [
    path('', home, name='home')
    path('print-message/', print_message, name='print_message')
]