from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

class Page(models.Model):
    title = models.CharField(max_length=255, verbose_name='Título')
    slug = models.SlugField(unique=True, blank=True)
    content = RichTextField(verbose_name='Contenido')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Página'
        verbose_name_plural = 'Páginas'
        ordering = ['title']