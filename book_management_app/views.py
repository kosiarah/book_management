from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from book_management_app.models import Book
from book_management_app.serializers import BookSerializer


@api_view(['POST'])
def add_book(request):
    if request.method == 'POST':
        data = request.data
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Message": "Book Added Successfully"}, serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def sell(request, id):
    if request.method == 'DELETE':
        try:
            book = Book.objects.get(id=id)
            book.delete()
            return Response({"Message": "Book sold"}, status=status.HTTP_204_NO_CONTENT)
        except Book.DoesNotExist:
            return Response({"Message": "Book not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_book(request, id):
    if request.method == 'GET':
        try:
            book = Book.objects.get(id=id)
            serializer = BookSerializer(book, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Book.DoesNotExist:
            return Response({"Message": "Book not found"}, status=status.HTTP_404_NOT_FOUND)