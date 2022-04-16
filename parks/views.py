from django.http import JsonResponse

# Create your views here.


def get_park(request):
    return JsonResponse({"name": "Richmond Park", "location": "Richmond upon Thames"})
