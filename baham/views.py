from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from baham.enum_types import VehicleType
from baham.models import VehicleModel


# Create your views here.
def view_home(request):
    template = loader.get_template('home.html')
    context = {
        'navbar': 'home',
    }
    return HttpResponse(template.render(context, request))


def view_aboutus(request):
    template = loader.get_template('aboutus.html')
    context = {
        'navbar': 'aboutus',
    }
    return HttpResponse(template.render(context, request))


def view_vehicles(request):
    template = loader.get_template('vehicles.html')
    vehicles = VehicleModel.objects.all().order_by('vendor')
    context = {
        'navbar': 'vehicles',
        'vehicles': vehicles
    }
    return HttpResponse(template.render(context, request))


def create_vehicle(request):
    template = loader.get_template('createvehicle.html')
    context = {
        'navbar': 'vehicles',
        'vehicle_types': [(t.name, t.value) for t in VehicleType]
    }
    return HttpResponse(template.render(context, request))


def save_vehicle(request):
    _vendor = request.POST.get('vendor')
    _model = request.POST.get('model')
    _type = request.POST.get('type')
    _capacity = request.POST.get('capacity')
    #TODO: Validations
    vehicleModel = VehicleModel(vendor=_vendor, model=_model, type=_type, capacity=_capacity)  #TODO:
    vehicleModel.save()
    return HttpResponseRedirect(reverse('vehicles'))
