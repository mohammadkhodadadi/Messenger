from django.core.management.base import BaseCommand
from faker import Faker
from django.contrib.auth import get_user_model
from api.models import Message, Chat, ChatMessage, Membership, Contact
from django.db.utils import IntegrityError
import random

fake = Faker()


class Command(BaseCommand):
    help = 'Populate the database with mock data'

    def handle(self, *args, **options):
        fake = Faker()

        # Create 10 users
        User = get_user_model()
        for _ in range(10):
            username = fake.user_name()
            email = fake.email()
            # password = fake.password()
            password = '12345678Mn'
            age = random.randint(18, 60)
            try:
                User.objects.create_user(username=username, email=email, password=password, age=age)
            except IntegrityError:
                # Handle the case where a user with the same username or email already exists
                pass

        # Create 100 messages with random types (TEXT, STICKER, FILE) and random owners
        message_types = ['T', 'S', 'F']
        users = User.objects.all()
        for _ in range(100):
            body = fake.text(max_nb_chars=200)
            type = random.choice(message_types)
            owner = random.choice(users)
            Message.objects.create(body=body, type=type, owner=owner)

        # Create 10 chats
        for _ in range(10):
            title = fake.text(max_nb_chars=150)
            type = 1  # Regular chat
            chat = Chat.objects.create(title=title, type=type)

            # Add 10 members to each chat
            members = random.sample(list(users), 10)
            for member in members:
                role = 1
                Membership.objects.create(person=member, chat=chat, role=role)

        # Create 100 contact records with random nicknames
        for _ in range(100):
            owner = random.choice(users)
            member = random.choice(users)
            nick_name = fake.first_name()
            Contact.objects.create(owner=owner, member=member, nick_name=nick_name)
