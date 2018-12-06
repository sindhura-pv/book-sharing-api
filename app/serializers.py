from app.models import Book
from rest_framework import serializers
from django.contrib.auth.models import User

class BookSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Book
        fields = ('url', 'name', 'isbn', 'pub_year', 'publisher', 'date_created', 'date_modified', 'owner')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    books = serializers.PrimaryKeyRelatedField(many=True, queryset=Book.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'books')
