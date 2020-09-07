from . import models
from django import forms
from rest_framework import serializers
from allauth.account.adapter import get_adapter
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User as Miner
from dj_rest_auth.registration.serializers import RegisterSerializer

def validate_name(name, fieldname, min_length=2):
    if min_length and len(name) < min_length:
        raise forms.ValidationError(
                _(f"{fieldname} must be a minimum of {min_length} characters."))

    if not name.isalpha():
        raise forms.ValidationError(
            _(f"{fieldname} must be Alphabetic characters."))
    return name

class CustomRegisterSerializer(RegisterSerializer):
    firstname = serializers.CharField(
        min_length=2,
        required=True
    )
    lastname = serializers.CharField(
        min_length=2,
        required=True
    )
    
    def validate_firstname(self, firstname):
        return validate_name(firstname, "firstname")

    def validate_lastname(self, lastname):
        return validate_name(lastname, "lastname")

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'firstname': self.validated_data.get('firstname', ''),
            'lastname': self.validated_data.get('lastname', ''),
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            'email': self.validated_data.get('email', '')
        }


class MinerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Miner
        fields = '__all__'
