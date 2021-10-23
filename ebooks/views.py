from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin

from .models import Ebook
from .serializers import EbookSerializer


class EbookListCreateAPIView(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
