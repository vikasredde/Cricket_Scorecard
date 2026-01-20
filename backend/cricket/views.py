from django.shortcuts import render
from rest_framework.views import APIView
from . import serializer
from . import models
from rest_framework.response import Response
from rest_framework import status

# def home(request):
#     teams=models.Team.objects.all()

#     # render(request, template_name, context)
#     return render(request,'cricket/home.html',{'teams':teams})



class AddballAPIVIEW(APIView):

    def post(self,request):
        serializers=serializer.Ballserializer(data=request.data)

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        

        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)



class Innings(APIView):
    def get(self,request,innnings_id):
        Innings=models.Innings.objects.get(id=innnings_id)
        serializers=serializer.InningsSerializer(Innings)
        return Response(serializers.data)



