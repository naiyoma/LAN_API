import uuid

from django.db import models

# uuid.uuid4
class User(models.Model):
    id = models.UUIDField(primary_key=True,
        default=1, editable=False)
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Category(models.Model):
    id = models.UUIDField(primary_key=True,
        default=1, editable=False)
    name = models.CharField(max_length=100)
    notes = models.TextField()
    user = models.ForeignKey(User,
        related_name="categories", on_delete=models.CASCADE)


    def __str__(self):
        return self.name
