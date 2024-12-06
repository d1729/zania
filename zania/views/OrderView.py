import json
import random

from django.http import JsonResponse
from rest_framework.views import APIView

from zania.service import getIdAndPrice


class OrderView(APIView):
    def post(self, request):
        body = request.body.decode('utf-8')
        data = json.loads(body)
        priceById = getIdAndPrice()
        price = 0.0
        for order in data:
            id, quantity = order['id'], order['quantity']
            if id in priceById:
                price += quantity * priceById[id]

        return JsonResponse({'orderId': random.randint(1, 10000000), 'price': price})

