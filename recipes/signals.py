from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

from core.utils import generate_random_string
from recipes.models import Recipe


@receiver(pre_save, sender=Recipe)
def add_slug_to_recipe(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.title)

