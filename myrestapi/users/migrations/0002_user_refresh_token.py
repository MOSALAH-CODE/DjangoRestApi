# Generated by Django 5.0.2 on 2024-02-25 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='refresh_token',
            field=models.TextField(blank=True, null=True),
        ),
    ]