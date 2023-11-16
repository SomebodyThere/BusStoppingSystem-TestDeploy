from django.contrib import admin

from .models import BusModel, Route, BusStation, Bus, Reserve, StationRoute, Dispatch

class BusModelAdmin(admin.ModelAdmin):
  list_display = ["model_name", "model_serial_number", "max_passenger", "engine", "low_floow_TF"]

admin.site.register(BusModel, BusModelAdmin)
admin.site.register(Route)
admin.site.register(BusStation)
admin.site.register(Bus)
admin.site.register(Dispatch)
admin.site.register(Reserve)
admin.site.register(StationRoute)