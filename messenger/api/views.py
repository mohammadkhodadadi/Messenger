from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet, mixins
from rest_framework.permissions import IsAuthenticated
from .models import Chat, Membership
from .serializers import ChatSerializer
from django.db.models import Prefetch
################################################################
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model

User = get_user_model()


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
        chats = Chat.objects.all()  # Retrieve all objects from your model
        if self.request.method in ['LIST']:

            prefetch_membership = Prefetch(
                'membership_set',
                queryset=Membership.objects.filter(role=2),
                to_attr='published_roles'
            )
            prefetch_person = Prefetch(
                'published_roles__person',
                queryset=User.objects.all(),
                to_attr='published_users'
            )
            chats = chats.prefetch_related(
                prefetch_membership,
                prefetch_person
            )

        # if self.request.method in ['DELETE', 'PUT']:
        #     query_set = query_set.filter(chat_id=self.kwargs['chat_id'])
        # chat_id = self.kwargs.get('pk')

        # if chat_id:
        #     query_set = Chat.objects.filter(chat_id=chat_id).select_related('membership')

        return query_set


@api_view(['GET'])
def your_model_list(request):
    # if request.method == 'GET':
    #     chats = Chat.objects.prefetch_related('membership_set__person').all()  # Retrieve all objects from your model
    #     # Iterate through the chats and access the related objects
    #     for chat in chats:
    #         print(f"Chat Title: {chat.title}")
    #
    #         # Access memberships for each chat
    #         for membership in chat.membership_set.all():
    #             print(f"Member: {membership.person.username}, Role: {membership.role}")
    #
    #         print("\n")
    #     # serializer = YourModelSerializer(queryset, many=True)
    #     return Response(status.HTTP_200_OK)
    out = []
    if request.method == 'GET':
        chats = Chat.objects.all()  # Retrieve all objects from your model

        prefetch_membership = Prefetch(
            'membership_set',
            queryset=Membership.objects.filter(role=2),
            to_attr='published_roles'
        )
        prefetch_person = Prefetch(
            'published_roles__person',
            queryset=User.objects.all(),
            to_attr='published_users'
        )

        XX = Prefetch(
            'membership_set__person',
            queryset=User.objects.all(),
            to_attr='zz'
        )
        chats = chats.prefetch_related(
            # prefetch_membership,
            # prefetch_person,
            XX
        )
        output = []
        for chat in chats:
            for member in chat.zz:
                output.append(member.username)
        return Response(output, status.HTTP_200_OK)

        # out1 = []
        # for chat in chats:
        #     print(f"Chat Title: {chat.title}")
        #
        #     # Access memberships for each chat
        #     for membership in chat.published_roles:
        #         print(f"Role: {membership.role}")
        #         out.append(membership.role)
        #
        #         m = membership.published_users  # Make sure 'published_users' is the correct attribute name
        #         print(f"User: {m.username}, Email: {m.email}")
        #         out1.append({"User": m.username, "Email": m.email})
        # print("\n")
        #
        # return Response(out1, status.HTTP_200_OK)

