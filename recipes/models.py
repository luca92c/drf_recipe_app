from django.db import models
from django.conf import settings


class Recipe(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=120, default="", null=False)
    content = models.TextField(null=True)
    ingredients = models.TextField(null=True)
    total_time = models.DurationField(blank=True, null=True)
    servings = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='../media', blank=True, null=True)
    slug = models.SlugField(max_length=255, blank=True, default="")
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name="recipes")

    def __str__(self):
        return self.title


class Comment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    body = models.TextField(max_length=140, default="")
    recipe = models.ForeignKey(Recipe,
                               on_delete=models.CASCADE,
                               related_name="comments")
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name="CASCADE")
    voters = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="votes")

    def __str__(self):
        return self.author.username

