from apii.models import Snippet
from django.shortcuts import render
from rest_framework import viewsets
from apii.models import *
from apii.serializers import *

from rest_framework.response import Response
from rest_framework import permissions



class SnippetViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

   