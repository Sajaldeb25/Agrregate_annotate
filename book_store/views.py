from django.db.models import Max, Avg, Count, Min
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
        pub = Publisher.objects.annotate(num_b=Count('book'))
        print(pub[2].num_b)

        return Response(serializer.data, status=status.HTTP_200_OK)


class BookView(APIView):
    def get(self, request):
        book = Book.objects.order_by('name')
        serializer = BookSerializer(book, many=True)
        cnt = Book.objects.count()
        print(cnt)  # print number of object in book table

        max_price = Book.objects.all().aggregate(Max('price'))
        print(max_price)

        avg_price = Book.objects.all().aggregate(Avg('price'))
        print(avg_price)

        Book.objects.aggregate(price_diff=Max('price') - Avg('price'))
        # print(price_diff)

        bb = Book.objects.aggregate(Avg('price'), Max('price'), Min('price'))
        print(bb)

        q = Book.objects.annotate(b_cnt=Count('authors'))
        print(q[0].b_cnt)
        print(q[1].b_cnt)
        print(q[2].b_cnt)
        print(q[3].b_cnt)
        # print(q[4].authors__count)

        book = Book.objects.order_by("name").select_related("publisher")

        # for bk in book:
        #     print(bk.name, "by", bk.authors.name)

        return Response(serializer.data, status=status.HTTP_200_OK)


class StoreView(APIView):
    def get(self, request):
        store = Store.objects.all()
        serializer = StoreSerializer(store, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

