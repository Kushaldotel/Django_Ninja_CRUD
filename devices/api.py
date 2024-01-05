from ast import List
from ninja import NinjaAPI
from .models import Device, Location
from .schemas import (
    DeviceSchema,
    LocationSchema,
    DeviceCreateSchema,
    ErrorSchema,
    DeviceLocationPatchSchema,
)
from django.shortcuts import get_object_or_404

api = NinjaAPI()


@api.get("devices/", response=list[DeviceSchema])
def list_devices(request):
    return Device.objects.all()


@api.get("devices/{slug}", response=DeviceSchema)
def get_device(request, slug: str):
    device = get_object_or_404(Device, slug=slug)
    return device


@api.get("locations/", response=list[LocationSchema])
def list_locations(request):
    return Location.objects.all()


@api.post("devices/", response={202: DeviceSchema, 404: ErrorSchema})
def create_device(request, device: DeviceCreateSchema):
    if device.location_id:
        location_exist = Location.objects.filter(id=device.location_id).exists()
        if not location_exist:
            return 404, {"message": "Location not found"}
    device_data = device.model_dump()
    device_model = Device.objects.create(**device_data)
    return device_model


@api.post("devices/{device_slug}/location/", response=DeviceSchema)
def update_device_location(request,device_slug: str, location: DeviceLocationPatchSchema):
    device = get_object_or_404(Device, slug=device_slug)
    if location.location_id:
        location = get_object_or_404(Location, id=location.location_id)
        device.location = location
    else:
        device.location = None

    device.save()
    return device
