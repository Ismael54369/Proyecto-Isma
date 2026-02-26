from django.contrib import admin
from .models import Especie, Rasgo, Animal, SolicitudAdopcion

admin.site.register(Especie)
admin.site.register(Rasgo)

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'especie', 'estado', 'fecha_nacimiento')
    list_filter = ('especie', 'estado', 'rasgos')
    search_fields = ('nombre',)

@admin.register(SolicitudAdopcion)
class SolicitudAdopcionAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'animal', 'estado', 'fecha_solicitud')
    list_filter = ('estado', 'fecha_solicitud')
    search_fields = ('usuario__username', 'animal__nombre')