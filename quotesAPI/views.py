from rest_framework import generics

from .models import Quote
from .pagenation import CustomePagenation
from .permissions import IsAdminUserOrReadOnly
from .serializers import QuoteSerializer


class QuoteListCreateAPIView(generics.ListCreateAPIView):
    queryset = Quote.objects.all().order_by("-id")
    serializer_class = QuoteSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    pagination_class = CustomePagenation


class QuoteDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    permission_classes = [IsAdminUserOrReadOnly]
