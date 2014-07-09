from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    photo = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=200, default="Yum.")
    prep_time = models.IntegerField(default=0)
    cook_time = models.IntegerField(default=0)
    num_servings = models.IntegerField(max_length=4, default=1)
    ingredients = models.ManyToManyField("Ingredient", null=True, blank=True)
    directions = models.TextField(default="Please enter instructions on how to create this amazing cuisine.")
    tag = models.ManyToManyField("RecipeTag")

    def __unicode__(self):
        return self.name


class RecipeTag (models.Model):
    name = models.CharField(max_length=50)

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
