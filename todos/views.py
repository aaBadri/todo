from rest_framework import generics
from todos.models import Todo
from todos.serializers import TodoSerializer 

# Create your views here.
class ListTodo(generics.ListAPIView):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

class DetailTodo(generics.RetrieveAPIView):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()