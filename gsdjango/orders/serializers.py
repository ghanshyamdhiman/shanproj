from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ['user_id, 'product_code']
          
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password', )
