from django.http import HttpResponse
from django.shortcuts import render

from .models import CPU

def index(request):
    cpu = CPU.objects.get(pk='34dc0a24-0dad-42fe-a662-86b93d68f2f7')
    context = {
        'cpu': cpu,
    }
    return render(request, 'hardware/index.html', context)