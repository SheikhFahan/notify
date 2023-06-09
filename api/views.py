from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from base1.models import Note
from base1.serializers import NoteSerializer
# Create your views here.

# @api_view(["GET"])
# def api_home(request, *args, **kwargs):
#     """retrieve data from the used for only notes now modify to work on all"""
#     instance = Note.objects.order_by("?").first()
#     data = {}
#     if instance:
#        data = NoteSerializer(instance).data
#     return Response(data)

@api_view(["POST"])
def api_home(request, *args, **kwargs):
    serializer = NoteSerializer(data= request.data)
    if serializer.is_valid():
        print(serializer.data)
        return Response(serializer.data)
    else:
        print(serializer.error_messages)
    return Response({"invalid" : "invalid data"})