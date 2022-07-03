from django.contrib.auth.models import User
from django.db import models


STATUS = (
    (0, "Draft"),
    (1, "Publish"),
    (2, "Archive"),
)


class Post(models.Model):

    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)

    author = models.ForeignKey(
        User,
        related_name="blog_posts",
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title