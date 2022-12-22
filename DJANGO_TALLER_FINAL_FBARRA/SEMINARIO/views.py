from django.shortcuts import render, redirect
from .serializers import ParticipantesSerializers, InstitucionesSerializers
from .models import Participantes, Instituciones
from .forms import ParticipantesForm
from rest_framework.response import Response 
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.http import Http404
from django.http import JsonResponse

# Create your views here.

#CRUD
def verAPI(request):
    part = Participantes.objects.all()
    data1 = ({'Participantes': list(part.values('id','nombre','telefono','fecha_inscripcion','hora_inscripcion','institucion','estado','observacion'))})
    return JsonResponse(data1)

def index(request):
    return render(request, 'index.html')

def listadoParticipantes(request):
    part = Participantes.objects.all()
    data = {'Participantes': part}
    return render(request,'listadoParticipantes.html',data)

def agregarParticipantes(request):
    form = ParticipantesForm()
    if request.method == 'POST':
        form = ParticipantesForm(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'agregarParticipantes.html', data)

def eliminarParticipantes(request,id):
    part = Participantes.objects.get(id = id)
    part.delete()
    return redirect('/listadoParticipantes')

def actualizarParticipantes(request,id):
    part = Participantes.objects.get(id = id)
    form = ParticipantesForm(instance=part)
    if request.method == 'POST':
        form = ParticipantesForm(request.POST, instance=part)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'agregarParticipantes.html', data)

#CLASES PARTICIPANTE
class ParticipantesLista (APIView):
    def get(self, request):
        part = Participantes.objects.all()
        serial = ParticipantesSerializers(part, many = True)
        return Response(serial.data)

    def post(self, request):
        serial = ParticipantesSerializers(data = request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
   
class ParticipantesDetalle(APIView):
    def get_object(self, pk):
        try:
            return Participantes.objects.get(id = pk)
        except Participantes.DoesNotExist:
            return Http404

    def get(self, request, pk):
        part = self.get_object(pk)
        serial = ParticipantesSerializers(part)
        return Response(serial.data)
    
    def put(self, request, pk):
        part = self.get_object(pk)
        serial = ParticipantesSerializers(part, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        part = self.get_object(pk)
        part.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#Instituciones
@api_view(['GET', 'POST'])
def Instituciones_Lista(request):
    if request.method == 'GET':
        ins = Instituciones.objects.all()
        serial = InstitucionesSerializers(ins, many=True)
        return Response(serial.data)
    
    if request.method == 'POST':
        serial = InstitucionesSerializers(data = request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def Instituciones_Detalle(request, pk):
    try:
        ins = Instituciones.objects.get(id = pk)
    except Instituciones.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serial = InstitucionesSerializers(ins)
        return Response(serial.data)

    if request.method == 'PUT':
        serial = InstitucionesSerializers(ins, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
            
    if request.method == 'DELETE':
        ins.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


                