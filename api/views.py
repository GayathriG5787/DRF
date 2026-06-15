# Converts Python dictionary into JSON
from rest_framework.response import Response
# Tells DRF that the fn is an API endpoint
# handles DRF features like request parsing (converting JSON into python objects) and giving response
from rest_framework.decorators import api_view

@api_view(['GET'])
def getData(request):
    person = {'name': 'Gayathri', 'age': 21}
    return Response(person)