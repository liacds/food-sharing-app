from django.shortcuts import render
from django.shortcuts import render
from rest_framework.status import *
from rest_framework.views import APIView
from authenticate.models import User
from .models import Food_Pack
from .serializers import Food_Pack_Serializer, Shorter_Food_Pack_Serializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
import datetime
from rest_framework import permissions
# Create your views here.


class IsCompany(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_company


class ProductCreateView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    serializer_class = Food_Pack_Serializer
    permission_classes = [IsCompany]

class GetAllShippedFoodPacks(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsCompany ]
    serializer_class = Food_Pack_Serializer
    def get(self, request):
        user = request.user
        complete_food_packs = Food_Pack.objects.filter(user=user, is_completed = True)
        serializer = Shorter_Food_Pack_Serializer(complete_food_packs, many=True)
        return Response(serializer.data, HTTP_200_OK)

class GetAllScheduledFoodPacks(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsCompany ]
    serializer_class = Food_Pack_Serializer
    def get(self, request):
        user = request.user
        complete_food_packs = Food_Pack.objects.filter(user=user, timestamp__gte = datetime.datetime.now())
        serializer = Shorter_Food_Pack_Serializer(complete_food_packs, many=True)
        return Response(serializer.data, HTTP_200_OK)

class NumberOfShippedFoodPacks(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsCompany]
    serializer_class = Food_Pack_Serializer

    def get(self, request):
        user = request.user
        complete_food_packs = len(Food_Pack.objects.filter(user=user, is_completed=True))
        return Response(str(complete_food_packs), HTTP_200_OK)