from rest_framework.response import Response 
from rest_framework.decorators import api_view
from . import utilities
# Create your views here.

@api_view(['GET'])
def always_success(request):
   return Response('works')

@api_view(['GET'])
def test(request):
   return Response(utilities.format_map('map0'))

