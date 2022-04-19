from django.db.models import Max
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Author, Publisher, Book, Store
from .serializer import AuthorSerializer, PublisherSerializer, BookSerializer, StoreSerializer

# Create your views here.


class AuthorView(APIView):
    def get(self, request):  # to see categories
        author = Author.objects.all()
        serializer = AuthorSerializer(author, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PublisherView(APIView):
    def get(self, request):  # to see categories
        publisher = Publisher.objects.all()
        serializer = PublisherSerializer(publisher, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BookView(APIView):
    def get(self, request):
        book = Book.objects.all()
        serializer = BookSerializer(book, many=True)
        cnt = Book.objects.count()
        print(cnt)  # print number of object in book table

        max_price = Book.objects.all().aggregate(Max('price'))
        print(max_price)
        return Response(serializer.data, status=status.HTTP_200_OK)


class StoreView(APIView):
    def get(self, request):
        store = Store.objects.all()
        serializer = StoreSerializer(store, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

