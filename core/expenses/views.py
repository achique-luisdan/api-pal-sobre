from django.shortcuts import render
from rest_framework import viewsets, parsers
from rest_framework import authentication
from .models import Expense, Goal
from .serializers import ExpenseSerializer, GoalSerializer
from rest_framework import permissions

class ExpenseViewset(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    authentication_classes = [authentication.TokenAuthentication ]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class GoalViewset(viewsets.ModelViewSet):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    authentication_classes = [authentication.TokenAuthentication ]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]