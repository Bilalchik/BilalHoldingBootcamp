from django.shortcuts import render, redirect

from .models import Car, Category


def index_view(request):
    cars = Car.objects.all()

    return render(request, 'app/index.html', {'cars': cars})


def car_detail_view(request, car_id):
    car = Car.objects.get(id=car_id)

    return render(request=request, template_name='app/car_detail.html', context={'car': car})


def car_create_view(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        title = request.POST['title']
        category_id = request.POST['category_id']
        model = request.POST['model']
        year = request.POST['year']
        price = request.POST['price']
        image = request.FILES['image']

        category = Category.objects.get(id=category_id)

        car = Car(title=title, category=category, model=model, year=year, price=price, image=image)
        car.save()

        return redirect('index')

    return render(request, 'app/car_create.html', context={'categories': categories})
