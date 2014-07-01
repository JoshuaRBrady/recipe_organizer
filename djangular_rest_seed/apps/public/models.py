from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=150, default="Yum.")
    ingredients = models.ManyToManyField("Ingredient")

    def __unicode__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    category = models.ManyToManyField("IngredientCategory")

    def __unicode__(self):
        return self.name


class IngredientCategory(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Ingredient Categories"

    def __unicode__(self):
        return self.name