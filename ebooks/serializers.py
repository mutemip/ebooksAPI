from rest_framework import serializers
from .models import Ebook, Reveiw


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reveiw
        fields = "__all__"


class EbookSerializer(serializers.ModelSerializer):
    review = ReviewSerializer(many=True, read_only=True)  # to make relationship between the two serializers explicit

    class Meta:
        model = Ebook
        fields = "__all__"
