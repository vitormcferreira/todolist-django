from django.contrib.auth.models import User
from django.db import models


class ToDoItem(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=255)
    text = models.TextField(blank=True)
