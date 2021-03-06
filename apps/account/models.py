from django.db import models
from django_extensions.db.models import TimeStampedModel


class User(TimeStampedModel):
    class Meta:
        ordering = ["user_id"]
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    user_id = models.BigIntegerField(unique=True, verbose_name="Telegram ID")
    name = models.CharField(max_length=100, verbose_name="Telegram имя")
    username = models.CharField(max_length=100, verbose_name="Telegram username")
    email = models.EmailField(max_length=100, null=True, verbose_name="Email")

    def __str__(self):
        return f"№{self.id} ({self.user_id} - {self.name})"


class Referral(TimeStampedModel):
    class Meta:
        verbose_name = "Реферал"
        verbose_name_plural = "Рефералы"

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    referrer = models.BigIntegerField(verbose_name="Реферал ID")

    def __str__(self):
        return f"№{self.user.id} - от {self.referrer}"
