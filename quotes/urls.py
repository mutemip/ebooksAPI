from django.urls import path
from .views import QuoteListAPIView, QuoteDetailAPIView

urlpatterns = [
    path('quotes/', QuoteListAPIView.as_view(), name='quotes-list'),
    path('quotes/<int:pk>/', QuoteDetailAPIView.as_view(), name='quotes-details'),

]