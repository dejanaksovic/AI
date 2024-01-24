from rest_framework.response import Response 
from rest_framework import status
from rest_framework.decorators import api_view
from . import utilities
# Create your views here.

@api_view(['GET'])
def always_success(request):
   return Response('works')

@api_view(['GET'])
def get_position(request):
   map = request.query_params.get("map")

   if not map:
      return Response({"Error": "you have to request a map"}, status = status.HTTP_400_BAD_REQUEST)

   if not map in ["map0", "map1"]:
      return Response({"Error": "invalid map name"}, status = status.HTTP_400_BAD_REQUEST)

   return Response(utilities.format_map_values(map)[0])
