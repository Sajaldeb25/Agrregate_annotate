from django.urls import path
from .views import AuthorView,PublisherView, BookView, StoreView

urlpatterns = [
    path('author/', AuthorView.as_view(), name='author'),
    path('publisher/', PublisherView.as_view(), name='publisher'),
    path('book/', BookView.as_view(), name='book'),
    path('store/', StoreView.as_view(), name='store'),
]
