from django.db import models
from django.utils import timezone


class ContactMessage(models.Model):
    name = models.CharField(max_length=100, verbose_name="Ism")
    surname = models.CharField(max_length=100, verbose_name="Familiya")
    phone = models.CharField(max_length=20, verbose_name="Telefon raqami")
    email = models.EmailField(verbose_name="Email manzili")
    message = models.TextField(verbose_name="Yuborilgan xabar")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Yuborilgan vaqt")

    def str(self):
        return f"{self.name} {self.surname}"

    class Meta:
        verbose_name = "Kontakt xabari"
        verbose_name_plural = "Kontakt xabarlari"
        ordering = ['-created_at']