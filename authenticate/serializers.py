from rest_framework import serializers
from django.contrib import auth
from .models import User
from rest_framework.exceptions import AuthenticationFailed



class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, min_length=8,
                                     write_only=True)
    is_company = serializers.BooleanField()
    class Meta:
        model = User
        fields = ['email', 'is_company', 'password', 'full_name', 'company_location']

    def validate(self, attrs):
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=255,
                                     min_length=8, write_only=True)
    email = serializers.EmailField(max_length=255, min_length=5)

    refresh_token = serializers.CharField(max_length=255,
                                          min_length=6, read_only=True)
    access_token = serializers.CharField(max_length=255,
                                         min_length=6, read_only=True)
    full_name = serializers.CharField(max_length=255,
                                          min_length=6, read_only=True)

    class Meta:
        model = User
        fields = ['pk', 'email', 'password',
                  'refresh_token', 'access_token', 'is_company', 'full_name']

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')

        user = auth.authenticate(email=email, password=password)

        if not user:
            raise AuthenticationFailed('User not found')

        tokens = user.tokens()
        return {
            'pk': user.pk,
            'email': user.email,
            'access_token': tokens['access'],
            'refresh_token': tokens['refresh'],
            'is_company': user.is_company,
            'full_name': user.full_name
        }