from django.db import models
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')
    slug = models.SlugField(max_length = 250, null = True, blank = True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)

        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

