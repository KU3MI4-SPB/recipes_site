from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    steps = models.TextField()
    cooking_time = models.PositiveIntegerField(help_text="в минутах")
    image = models.ImageField(upload_to='recipes/', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes')
    categories = models.ManyToManyField(Category, through='RecipeCategory')
    ingredients = models.TextField(help_text="разделённые запятыми", blank=True)

    def __str__(self):
        return self.title

class RecipeCategory(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('recipe', 'category')
