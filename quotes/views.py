from rest_framework import generics
from .serializers import QuoteSerializer
from .permissions import IsAdminUserOrReadOnly
from .models import Quote


class QuoteListAPIView(generics.ListAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer

class QuoteDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    permission_classes = [IsAdminUserOrReadOnly]