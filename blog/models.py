from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Título')
    subtitle = models.CharField(max_length=255, verbose_name='Subtítulo')
    content = RichTextField(verbose_name='Contenido')
    image = models.ImageField(upload_to='posts/', verbose_name='Imagen')
    created_at = models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Autor', default=1)  

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Publicación'
        verbose_name_plural = 'Publicaciones'
        ordering = ['-created_at']

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(verbose_name='Comentario')
    created_on = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    approved = models.BooleanField(default=False, verbose_name='Aprobado')

    class Meta:
        ordering = ['created_on']
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'

    def __str__(self):
        return f'Comentario de {self.author.username} en {self.post.title}'