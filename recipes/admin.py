from django.contrib import admin
from recipes.models import Recipe, Comment


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'servings', 'total_time')


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Comment)
