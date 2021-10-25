from django.urls import path
from .views import (EbookListCreateAPIView, DetailAPIView,
                    ReviewCreateAPIView, ReviewDetailAPIView)

urlpatterns = [
    path("ebooks/", EbookListCreateAPIView.as_view(), name="ebooks-list"),
    path('ebooks/<int:pk>/', DetailAPIView.as_view(), name="ebook-details"),
    path('ebooks/<int:ebook_pk>/review/', ReviewCreateAPIView.as_view(), name="ebook-review"),
    path('reviews/<int:pk>/', ReviewDetailAPIView.as_view(), name="review-detail")
]
