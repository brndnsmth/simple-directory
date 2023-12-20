import uuid
from django.db import models

# Add additional fields, as needed.

class Person(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    biography = models.TextField()
    name = models.CharField(max_length=200, blank=True, editable=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def save(self, *args, **kwargs):
        self.name = f"{self.first_name} {self.last_name}"
        super().save(*args, **kwargs)