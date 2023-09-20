# Generated by Django 3.2.7 on 2023-09-20 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='message',
        ),
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.chat')),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.message')),
            ],
        ),
        migrations.AddField(
            model_name='chat',
            name='messages',
            field=models.ManyToManyField(through='api.ChatMessage', to='api.Message'),
        ),
    ]
