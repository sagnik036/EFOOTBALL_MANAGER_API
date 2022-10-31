from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models import *
from .info import *
from .serializers import *
from api.common.errors import *
from django.db.models import Q


# # Create your views here.
# class UserView(APIView):
    
#     """an api to fetch basic user/players details"""
#     @classmethod
#     def get(cls, request):
#         pass
