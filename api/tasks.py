from celery import shared_task
from .models import Planet
from .services import fetch_all_planets

@shared_task
def store_planets():
    planets_data = fetch_all_planets()
    for planet_data in planets_data:
        Planet.objects.create(
            name=planet_data['name'],
            population=planet_data['population'] or None,
            terrains=','.join(planet_data['terrains']),
            climates=','.join(planet_data['climates'])
        )