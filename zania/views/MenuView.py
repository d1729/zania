import json

from django.http import JsonResponse
from rest_framework.views import APIView

from zania.service import findPizzaByName


class MenuView(APIView):
    def get(self, request):
        name = request.query_params.get('name')
        pizza = findPizzaByName(name)
        return JsonResponse(pizza) 

