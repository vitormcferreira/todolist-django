from django.db import models
from django.contrib.auth.models import User


class ToDoItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=255)
    text = models.TextField(blank=True)
