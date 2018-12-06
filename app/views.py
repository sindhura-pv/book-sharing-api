# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from rest_framework import permissions
from app.models import Book
from rest_framework import viewsets
from app.serializers import BookSerializer
from django.http import Http404
from app.permissions import IsOwnerOrReadOnly
from rest_framework import status
from rest_framework.response import Response


class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows books to be viewed or edited.
    """
    permission_classes = (permissions.IsAuthenticated,IsOwnerOrReadOnly,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
