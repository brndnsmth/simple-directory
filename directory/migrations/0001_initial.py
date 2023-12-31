# Generated by Django 4.2.8 on 2023-12-20 22:14

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('biography', models.TextField()),
                ('name', models.CharField(blank=True, editable=False, max_length=200)),
            ],
        ),
    ]
