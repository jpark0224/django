from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.


def get_park(request):
    return JsonResponse({"name": "Richmond Park", "location": "Richmond upon Thames"})
