from ninja import ModelSchema, Schema
from .models import Device, Location

class LocationSchema(ModelSchema):
    class Meta:
        model = Location
        fields = ('id', 'name')

class DeviceSchema(ModelSchema):
    location: LocationSchema | None = None
    class Meta:
        model = Device
        fields = ('id', 'name', 'slug', 'location')

class DeviceCreateSchema(Schema):
    name: str
    location_id: int | None = None

class ErrorSchema(Schema):
    message: str

class DeviceLocationPatchSchema(Schema):
    location_id: int | None = None