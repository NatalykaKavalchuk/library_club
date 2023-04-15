from PIL import Image
from django.db import models
from django.utils.text import slugify


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=201, unique=True, db_index=True, verbose_name='URL')
    bio = models.TextField()
    photo = models.ImageField(upload_to="author_photo", default="male-avatar-profile.jpg", blank=True, null=True)
    time_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(f'{self.first_name} {self.last_name}')
        return super().save(*args, **kwargs)


class Book(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=201, unique=True, db_index=True, verbose_name='URL', blank=True, null=True)
    description = models.TextField()
    author = models.ManyToManyField("Author", related_name='books')
    poster = models.ImageField(upload_to="poster", default="book-image.jpg", blank=True, null=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
