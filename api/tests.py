import json

from django.test import Client, TestCase
from django.urls import reverse
from rest_framework import status

from .models import Planet
from .serializers import PlanetSerializer


class PlanetAPITestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.planet = Planet.objects.create(name="Earth", population=7000000000, terrains="Mountains, Plains", climates="Tropical, Temperate")
        self.valid_payload = {
            'name': 'Mars',
            'population': 0,
            'terrains': 'Rocks, Mountains',
            'climates': 'Dry, Cold'
        }
        self.invalid_payload = {
            'name': '',
            'population': 0,
            'terrains': 'Rocks, Mountains',
            'climates': 'Dry, Cold'
        }

    def test_get_planets(self):
        response = self.client.get(reverse('get_planets'))
        planets = Planet.objects.all()
        serializer = PlanetSerializer(planets, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_valid_planet(self):
        response = self.client.post(reverse('create_planet'), data=self.valid_payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_planet(self):
        response = self.client.post(reverse('create_planet'), data=self.invalid_payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_planet(self):
        response = self.client.put(
            reverse('update_planet', kwargs={'pk': self.planet.pk}),
            data=json.dumps(self.valid_payload),  # Convert data to JSON string
            content_type='application/json'  # Set content type header
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_planet(self):
        response = self.client.delete(reverse('delete_planet', kwargs={'pk': self.planet.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)