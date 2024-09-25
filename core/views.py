from rest_framework import viewsets
from django.utils import timezone
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Restaurant, Menu, Vote, Employee
from .serializers import RestaurantSerializer, MenuSerializer, EmployeeSerializer, VoteSerializer


class EmployeeCreateView(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    http_method_names = ['post']
    permission_classes = [IsAuthenticatedOrReadOnly]


class RestaurantCreateView(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    http_method_names = ['post']
    permission_classes = [IsAuthenticatedOrReadOnly]


class MenuViewSet(viewsets.ModelViewSet):
    today = timezone.now().date()
    queryset = Menu.objects.filter(day=today)
    serializer_class = MenuSerializer
    http_method_names = ['post', 'get']
    permission_classes = [IsAuthenticatedOrReadOnly]


class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    http_method_names = ['post', 'get']
    permission_classes = [IsAuthenticatedOrReadOnly]