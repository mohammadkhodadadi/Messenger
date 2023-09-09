from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Message(models.Model):
    STICKER = 'S'
    TEXT = 'T'
    FILE = 'F'

    MESSAGE_TYPE = [
        (STICKER, 'S'),
        (TEXT, 'T'),
        (FILE, 'F'),
    ]
    body = models.TextField(max_length=200, blank=False)
    type = models.CharField(
        max_length=1, choices=MESSAGE_TYPE, default=TEXT)
    insert_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)


class Chat(models.Model):
    message = models.ManyToManyField(Message)
    type = models.SmallIntegerField(default=1)  # MESSAGE_TYPE = 1 means regular chat


class Contact(models.Model):
    member = models.ForeignKey(User, on_delete=models.PROTECT)
    nick_name = models.CharField(max_length=50, default="")
