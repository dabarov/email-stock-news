from django.db import models


class UserSubscription(models.Model):
    email = models.EmailField()
    ticker = models.CharField(max_length=50)
    active = models.BooleanField()

    class Meta:
        unique_together = ("email", "ticker")
