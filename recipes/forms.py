from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'steps', 'cooking_time', 'image', 'ingredients', 'categories']
        labels = {
            'title': 'Название',
            'description': 'Описание',
            'steps': 'Шаги приготовления',
            'cooking_time': 'Время приготовления',
            'image': 'Изображение',
            'ingredients': 'Ингредиенты',
            'categories': 'Категории',
        }
        widgets = {
            'categories': forms.CheckboxSelectMultiple,
        }
