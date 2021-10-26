from django.urls import path
from .views import QuoteListCreateAPIView, QuoteDetailAPIView

urlpatterns = [
    path('quotesAPI/', QuoteListCreateAPIView.as_view(), name='quotesAPI-list'),
    path('quotesAPI/<int:pk>/', QuoteDetailAPIView.as_view(), name='quotesAPI-details'),

]