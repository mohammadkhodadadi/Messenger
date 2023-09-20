from rest_framework import serializers
from .models import Chat, Membership
from django.db import transaction


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user

        with transaction.atomic():
            chat = Chat.objects.create(**validated_data)
            Membership.objects.create(chat=chat, person=user, role=3)  # role 3 is the admin.
            return chat
        raise serializers.ValidationError(f"Error while creating the entry new chat")
