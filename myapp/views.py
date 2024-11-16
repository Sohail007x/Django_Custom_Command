from django.shortcuts import render, redirect
from django.core.management import call_command
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def home(request):
    return render(request, 'myapp/home.html')

@csrf_exempt
def print_message(request):
    if request.method == 'POST':
        try:
            call_command('print_message')
            messages.success(request, 'Message printed successfully')
        except Exception as e:
            messages.error(request, f'Error printing message: (e)')
            return redirect('/')
        
        else:
            return redirect('/')
