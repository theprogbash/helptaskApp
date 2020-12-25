from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    user_image = models.FileField(_('Şəkil'), upload_to='static/images/', blank=True)
    phone_number = models.CharField(_('Telefon'), max_length=20, blank=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Aytişnik'
        verbose_name_plural = 'Aytişniklər'