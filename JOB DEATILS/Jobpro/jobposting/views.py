from django.shortcuts import render
from .serializers import *
from .models import JobPost
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def ListEl(request):
    ListEl1 = JobPost.objects.all()
    serializer = Jobserializers(ListEl1,many=True)
    return Response(serializer.data)



@api_view(['POST'])
def PostEl(request):
    ListEl2 = JobPost.objects.all()
    serializer = Jobserializers(data=request.data)
    if serializer. is_valid():
        serializer.save()
    return Response(serializer.data)



@api_view(['POST'])
def PutEl(request,id):
    jonobj = JobPost.objects.get(id=id)
    serializer = Jobserializers(instance=jonobj,data=request.data)
    if serializer. is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(["DELETE"])
def DeleteEl(request,id):
    jonobj = JobPost.objects.get(id=id)
    jonobj.delete()
    return Response("This job post was deleted")
