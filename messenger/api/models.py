from django.db import models


# Create your models here.
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
