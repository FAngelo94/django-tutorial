
# todo/views.py

from django.shortcuts import render
from rest_framework import viewsets          # add this
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from rest_framework import status
from .serializers import TodoSerializer
from .models import Todo                     # add this

# Enable only Get


class TodoViewList(APIView):       
      """
      List all todos, or create a new todo.
      """
      def get(self, request, format=None):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)


      def post(self, request, format=None):
            serializer = TodoSerializer(data=request.data)
            if serializer.is_valid():
                  serializer.save()
                  return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

      @classmethod
      def get_extra_actions(cls):
            return []


class TodoViewDetail(APIView):       # add this
      """
      Retrieve, update or delete a todo instance.
      """
      def get_object(self, pk):
            try:
                  return Todo.objects.get(pk=pk)
            except Todo.DoesNotExist:
                  raise status.HTTP_400_BAD_REQUEST

      def get(self, request, pk, format=None):
            todo = self.get_object(pk)
            serializer = TodoSerializer(todo)
            return Response(serializer.data)

      def put(self, request, pk, format=None):
            todo = self.get_object(pk)
            serializer = TodoSerializer(todo, data=request.data)
            if serializer.is_valid():
                  serializer.save()
                  return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

      def delete(self, request, pk, format=None):
            todo = self.get_object(pk)
            todo.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

      @classmethod
      def get_extra_actions(cls):
            return []

class FileUploadView(APIView):
    parser_classes = (FileUploadParser, )

    def post(self, request, format='jpg'):
        up_file = request.FILES['file']
        destination = open('/images/' + up_file.name, 'wb+')
        for chunk in up_file.chunks():
            destination.write(chunk)
        destination.close()  # File should be closed only after all chuns are added

        # ...
        # do some stuff with uploaded file
        # ...
        return Response(up_file.name, status.HTTP_201_CREATED)