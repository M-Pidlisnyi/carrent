from django.db import connection
from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import ModelFormMixin 
from .models import BodyStyle, Brand, Car, CarInstance

# Create your views here.
def index(request):
    """view function form home page"""
    carNum = Car.objects.all().count()
    instancesNum = CarInstance.objects.all().count()

    availableInstances = CarInstance.objects.filter(status__exact='a').count()

    brandNum = Brand.objects.all().count()

    context = {
        'carNum': carNum,
        'instancesNum': instancesNum,
        'availableInstances': availableInstances,
        'brandNum': brandNum
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class  CarListView(generic.ListView):
    model = Car
    paginate_by = 5

class CarDetailView(generic.DetailView):
    model = Car

class BrandListView(generic.ListView):
    model = Brand
    paginate_by = 5
    
class BrandDetailView(generic.DetailView):
    model = Brand
