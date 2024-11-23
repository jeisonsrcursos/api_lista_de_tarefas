from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from todo_api.models import Todo
from todo_api.serializers import TodoSerializer
from app.permissions import GlobalDefaultPermission


class TodoCreateListView(generics.ListCreateAPIView):
    #permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

# fake store

