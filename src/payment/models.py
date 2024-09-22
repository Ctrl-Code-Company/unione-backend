from django.contrib.auth import get_user_model
from django.db import models

USER = get_user_model()


class Order(models.Model):
    user = models.ForeignKey(USER, on_delete=models.CASCADE)
    total = models.IntegerField(default=0)
    is_finished = models.BooleanField(default=False)
    type = models.CharField(
        max_length=255, choices=[
            ('basic', 'basic'),
            ('pro', 'pro'),
            ('premium', 'premium')
        ]
    )
    payment = models.CharField(
        max_length=255, choices=[
            ("payme", "payme"),
            ("click", "click")
        ]
    )

    def __str__(self):
        return f"{self.id} {self.total}"

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"
