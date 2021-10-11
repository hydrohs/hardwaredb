from django.http import HttpResponse
from django.shortcuts import render

from .models import CPU

def index(request):
    cpu = CPU.objects.get(pk=1)
    context = {
        'cpu': cpu,
    }
    return render(request, 'hardware/index.html', context)