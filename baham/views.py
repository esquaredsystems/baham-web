from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.template import loader
from django.urls import reverse

from baham.enum_types import VehicleType
from baham.models import VehicleModel


# Create your views here.


def veh_delete(request, pk):
    vehicle_model = VehicleModel.objects.get(model_id=pk)
    vehicle_model.void()
    return HttpResponseRedirect(reverse('home'))

def veh_nodelete(request, pk):
    vehicle_model = VehicleModel.objects.get(model_id=pk)
    vehicle_model.unvoid()
    return HttpResponseRedirect(reverse('home'))

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
    vehicles = VehicleModel.objects.all().filter(is_deleted=False).order_by('vendor')
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
    _capacity = int(request.POST.get('capacity'))
    if not _vendor or not _model:
        return HttpResponseBadRequest('Manufacturer and Model name fields are mandatory!')
    if not _capacity or _capacity < 2:
        _capacity = 2 if _type == VehicleType.MOTORCYCLE else 4
    vehicleModel = VehicleModel(vendor=_vendor, model=_model, type=_type, capacity=_capacity)
    vehicleModel.save()
    return HttpResponseRedirect(reverse('vehicles'))
