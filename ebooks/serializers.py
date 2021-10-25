from rest_framework import serializers
from .models import Ebook, Reveiw


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reveiw
        exclude = ("ebook", )


class EbookSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)  # to make relationship between the two serializers explicit

    class Meta:
        model = Ebook
        fields = "__all__"
