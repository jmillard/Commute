from locations.models import Location, City, State,Zipcode
from django.contrib import admin

class CityAdmin(admin.ModelAdmin):
    prepopulated_fields = {"city_slug": ("city",)}

class StateAdmin(admin.ModelAdmin):
    prepopulated_fields = {"state_slug": ("state",)}

class ZipcodeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"zipcode_slug": ("zipcode",)}

admin.site.register(Location)
admin.site.register(City, CityAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(Zipcode, ZipcodeAdmin)
