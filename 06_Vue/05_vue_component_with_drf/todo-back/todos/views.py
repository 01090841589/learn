from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib.auth import get_user_model
from .models import Todo
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import TodoSerializer, UserCreationSerializer, UserSerializer
from rest_framework.decorators import api_view, permission_classes
# Create your views here.

User = get_user_model()

@api_view(['POST'])
def todo_create(request):
    serializer = TodoSerializer(data=request.POST)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(status=400)

@api_view(['PUT', 'DELETE'])
def todo_update_delete(request, id):
    todo = get_object_or_404(Todo, pk=id)
    if request.method == 'PUT':
        serializer = TodoSerializer(todo, data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=400)
    elif request.method == 'DELETE':
        todo.delete()
        return Response(status=204)

@api_view(['POST'])
@permission_classes((AllowAny, ))
def user_signup(request):
    serializer = UserCreationSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.set_password(request.data.get('password'))
        user.save()
        return Response({'message': '회원가입완료'})

@api_view(['POST'])
def user_detail(request, id):
    user = get_object_or_404(User, pk=id)
    if request.user != user:
        return HttpResponseForbidden()
    serializer = UserSerializer(user)
    return Response(serializer.data)