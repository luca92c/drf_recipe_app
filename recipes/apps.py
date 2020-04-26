from django.apps import AppConfig


class RecipeConfig(AppConfig):
    name = 'recipes'

    def ready(self):
        import recipes.signals
