from django.db import models
from django.urls import reverse

class Post(models.Model):
    text = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return 'Post #{}'.format(self.id)

    def get_absolute_url(self):
        return reverse('index')

    class Meta:
        verbose_name_plural = 'posts'

