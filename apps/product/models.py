from django.db import models
from django_extensions.db.models import TimeStampedModel
from jsonfield import JSONField

from apps.account.models import User


class Category(TimeStampedModel):
    class Meta:
        ordering = ["name"]
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    name = models.CharField("Название", max_length=100)

    def __str__(self):
        return f"№{self.id} - {self.name}"


class Item(TimeStampedModel):
    class Meta:
        ordering = ("-id",)
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    name = models.CharField("Название товара", max_length=50)
    photo = models.CharField("Фото file_id", max_length=200)
    price = models.DecimalField(decimal_places=2, max_digits=8, verbose_name="Цена")
    description = models.TextField(verbose_name="Описание", null=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET(0), verbose_name="Категория"
    )
    is_published = models.BooleanField("Опубликовано", default=False)

    def __str__(self):
        return f"{self.id} - {self.name}"


class Purchase(TimeStampedModel):
    class Meta:
        verbose_name = "Покупка"
        verbose_name_plural = "Покупки"

    buyer = models.ForeignKey(User, on_delete=models.SET(0), verbose_name="Покупатель")
    item = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name="Товар")
    amount = models.DecimalField(
        decimal_places=2, max_digits=8, verbose_name="Стоимость"
    )
    purchase_time = models.DateTimeField(
        auto_now_add=True, verbose_name="Время покупки"
    )
    shipping_address = JSONField(null=True, verbose_name="Адрес доставки")
    phone_number = models.CharField("Номер телефона", max_length=12)
    email = models.EmailField("Email", max_length=100, null=True)
    receiver = models.CharField("Имя получателя", max_length=100, null=True)
    successful = models.BooleanField("Оплачено", default=False)

    def __str__(self):
        return f"№{self.id} - {self.item} ({self.amount})"
