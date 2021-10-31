from django.db import connection
from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import ModelFormMixin 
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import BodyStyle, Brand, Car, CarInstance

# Create your views here.
def index(request):
    """view function form home page"""
    carNum = Car.objects.all().count()
    instancesNum = CarInstance.objects.all().count()

    availableInstances = CarInstance.objects.filter(status__exact='a').count()

    brandNum = Brand.objects.all().count()
    
    visits_num = request.session.get('visits_num', 0)
    request.session['visits_num'] = visits_num + 1

    context = {
        'carNum': carNum,
        'instancesNum': instancesNum,
        'availableInstances': availableInstances,
        'brandNum': brandNum,
        'visits_num': visits_num
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

class OnRentView(LoginRequiredMixin, generic.ListView):
    """Generic class-based view listing cars on rent to current user."""
    model = CarInstance
    template_name ='catalog/on_rent_view.html'
    paginate_by = 5

    def get_queryset(self):
        return CarInstance.objects.filter(renter=self.request.user).filter(status__exact="o").order_by("due_back")