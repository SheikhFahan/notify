from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from base1.models import Note
from base1.serializers import NoteSerializer
# Create your views here.

@api_view(["GET"])
def api_home(request, *args, **kwargs):
    serializer = NoteSerializer(request.data)
    if serializer:
        print(request.data)
        print(serializer.data)
        data = serializer.data
    return Response(data)