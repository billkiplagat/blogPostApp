from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    # To return title name instead of object name in admin dash
    def __str__(self):
        return self.title
