from rest_framework import generics
from rest_framework import permissions

from .serializers import QuoteSerializer
from .permissions import IsAdminUserOrReadOnly
from .pagenation import CustomePagenation
from .models import Quote


class QuoteListCreateAPIView(generics.ListCreateAPIView):
    queryset = Quote.objects.all().order_by("-id")
    serializer_class = QuoteSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    pagination_class = CustomePagenation


class QuoteDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    permission_classes = [IsAdminUserOrReadOnly]
