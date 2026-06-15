# Converts Python dictionary into JSON
from rest_framework.response import Response
# Tells DRF that the fn is an API endpoint
# handles DRF features like request parsing (converting JSON into python objects) and giving response
from rest_framework.decorators import api_view

from base.models import Item
from .serializers import ItemSerializer

@api_view(['GET'])
def getData(request):
    items = Item.objects.all()
    # serializer is itself an object and serializer.data contains dictionary of items, which will later be converted into JSON inside Response class
    serializer = ItemSerializer(items, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def addItem(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        
    return Response(serializer.data)