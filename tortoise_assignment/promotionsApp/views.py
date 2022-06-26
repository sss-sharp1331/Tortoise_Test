from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework import serializers, status
from rest_framework.response import Response

# Create your views here.


class PlanView(APIView):

    def get(self, request, format=None):
        snippets = PlanInfo.objects.all()
        serializer = PlanInfoSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PlanInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Account has been created successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserView(APIView):

    def get(self, request, format=None):
        snippets = UserData.objects.all()
        serializer = UserSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Account has been created successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
