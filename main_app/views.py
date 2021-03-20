from django.shortcuts import render
from django.shortcuts import render
from rest_framework.status import *

from authenticate.models import User
from .models import Food_Pack
from .serializers import Food_Pack_Serializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework import filters
from rest_framework import permissions
# Create your views here.


class IsCompany(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_company

class ProductCreateView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    serializer_class = Food_Pack_Serializer
    permission_classes = [IsCompany]