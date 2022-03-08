from django.contrib import admin

from measurement.models import Measurment, Sensors

# Register your models here.


@admin.register(Sensors)
class SensorAdmin(admin.ModelAdmin):
    pass


@admin.register(Measurment)
class MeasurementAdmin(admin.ModelAdmin):
    pass
