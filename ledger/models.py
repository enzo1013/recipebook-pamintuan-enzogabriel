from django.db import models
from django.urls import reverse

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('ledger:detail', args=[self.pk])

    def __str__(self):
        return self.name
    
class Recipe(models.Model):
    name = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('ledger:detail', args=[self.pk])

    def __str__(self):
        return self.name
    
class RecipeIngredient(models.Model):
    quantity = models.ForeignKey(
                            Ingredient,
                            on_delete = models.SET_NULL,
                            null = True,
                            related_name = 'quantity'
                            )
    
    ingredient = models.ForeignKey(
                                Ingredient,
                                on_delete = models.SET_NULL,
                                null = True,
                                related_name = 'recipe'
                                )
    recipe = models.ForeignKey(
                            Recipe,
                            on_delete = models.SET_NULL,
                            null = True,
                            related_name = 'ingredients'
                            )
    
    def __str__(self):
        return self.name