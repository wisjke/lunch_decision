from rest_framework import serializers
from .models import Restaurant, Menu, Vote, Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['name']


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'address']


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'restaurant', 'day', 'items']


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['employee', 'menu', 'voted_at']
