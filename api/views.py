from rest_framework.response import Response
from rest_framework.decorators import api_view
from .utils import convert_currency
from django.shortcuts import render


@api_view(['GET'])
def convert(request):
    amount = float(request.query_params.get('amount', 0))
    result = convert_currency(amount)
    return Response({'amount_in_usd': result})
def index(request):
    return render(request, 'index.html')