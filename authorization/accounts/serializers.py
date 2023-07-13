from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from phonenumber_field.serializerfields import PhoneNumberField

from .models import User


class RegisterUser(ModelSerializer):
    phone_number = PhoneNumberField()

    class Meta:
        model = User
        fields = ["name", "phone_number"]


class BirthDaySerializer(ModelSerializer):
    birth_day = serializers.DateField()

    class Meta:
        model = User
        fields = ['birth_day']


class PhoneNumberSerializer(ModelSerializer):
    phone_number = PhoneNumberField()

    class Meta:
        model = User
        fields = ["phone_number"]
