from rest_framework import serializers
from .models import Participantes, Instituciones

class ParticipantesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Participantes
        fields = '__all__'

class InstitucionesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Instituciones
        fields = '__all__'