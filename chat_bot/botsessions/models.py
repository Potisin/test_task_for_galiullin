from django.db import models

from users.models import CustomUser


class BotSession(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    step = models.IntegerField(default=0)
    data = models.JSONField(default=dict)
    