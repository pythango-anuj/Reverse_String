from rest_framework.response import Response
from rest_framework.decorators import api_view
import json

# Create your views here.

# INPUT SAMPLE
'''
{

'string_to_reverse' : "I am Anuj Pandey"

}
'''

@api_view(['POST'])
def reverse_string(request):
    if request.method == "POST":
        string_to_reverse = request.data['string_to_reverse']
        reversed_string = string_to_reverse[::-1]
        response_data = {'original string':string_to_reverse,'reversed_string':reversed_string}
        print(response_data)
        return Response(response_data)
