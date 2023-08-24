from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.
def get(self, request, format=None):
    return JsonResponse({"message":
    'FUTURE HOME OF AWESOME THINGS'})