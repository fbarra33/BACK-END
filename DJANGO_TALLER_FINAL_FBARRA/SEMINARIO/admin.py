from django.contrib import admin
from .models import Participantes

# Register your models here.

class ParticipantesAdmin(admin.ModelAdmin):
    list_display = ['nombre','institucion','estado']

admin.site.register(Participantes, ParticipantesAdmin)

