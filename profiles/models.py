from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, verbose_name='Avatar')
    bio = models.TextField(blank=True, verbose_name='Biografía')
    link = models.URLField(blank=True, verbose_name='Enlace')
    birth_date = models.DateField(blank=True, null=True, verbose_name='Fecha de Cumpleaños')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'