from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet, GenericViewSet, mixins
from .models import Chat
from .serializers import ChatSerializer


# Create your views here.
class ChatViewSet(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  GenericViewSet):

    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
