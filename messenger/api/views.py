from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet, mixins
from rest_framework.permissions import IsAuthenticated
from .models import Chat
from .serializers import ChatSerializer


# Create your views here.
class ChatViewSet(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.RetrieveModelMixin,
                  GenericViewSet):
    # queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = [IsAuthenticated]

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data, context={'request': request})
    #     serializer.is_valid(raise_exception=True)
    #     authenticated_user = self.request.user
    #     self.perform_create(serializer)

    # def get_permissions(self):
    #     pass
    def get_serializer_context(self):
        # Get the `chat_pk` from the URL kwargs
        chat_pk = self.kwargs.get('pk')
        # Pass it to the serializer context
        return {'chat_pk': chat_pk}

    def get_queryset(self):
        query_set = Chat.objects.all()
        if self.request.method in ['LIST']:
            query_set = query_set.filter()
        # if self.request.method in ['DELETE', 'PUT']:
        #     query_set = query_set.filter(chat_id=self.kwargs['chat_id'])
        chat_id = self.kwargs.get('pk')

        if chat_id:
            query_set = Chat.objects.filter(chat_id=chat_id).select_related('membership')

        return query_set
