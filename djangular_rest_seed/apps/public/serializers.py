__author__ = 'Joshua'

from models import *
from rest_framework import serializers

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient