from django.shortcuts import render
from .models import Car


def index_view(request):
    cars = Car.objects.all()

    return render(request, 'app/index.html', {'cars': cars})


# представьте что мы написали большую логику
