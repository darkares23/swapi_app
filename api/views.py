
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Planet
from .serializers import PlanetSerializer
from .tasks import store_planets


@api_view(['GET'])
def get_planets(request):
    planets = Planet.objects.all()
    serializer = PlanetSerializer(planets, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_planet(request):
    serializer = PlanetSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_planet(request, pk):
    planet = Planet.objects.get(pk=pk)
    serializer = PlanetSerializer(planet, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_planet(request, pk):
    planet = Planet.objects.get(pk=pk)
    planet.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


def populate(request):
    store_planets.delay()
    return JsonResponse({"status": "Fetching and storing planets task enqueued."})