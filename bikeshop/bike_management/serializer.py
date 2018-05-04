from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from .models import Book, Category


class Categoryserializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'slug')


# Serializers define the API representation.
class Bookserializer(serializers.ModelSerializer):
    category = Categoryserializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ('name', 'publish_date', 'category', 'detail', 'images')
