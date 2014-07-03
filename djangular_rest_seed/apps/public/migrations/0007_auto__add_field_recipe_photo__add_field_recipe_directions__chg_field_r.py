# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Recipe.photo'
        db.add_column(u'public_recipe', 'photo',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Recipe.directions'
        db.add_column(u'public_recipe', 'directions',
                      self.gf('django.db.models.fields.TextField')(default='Please enter instructions on how to create this amazing cuisine.'),
                      keep_default=False)


        # Changing field 'Recipe.description'
        db.alter_column(u'public_recipe', 'description', self.gf('django.db.models.fields.CharField')(max_length=200))

    def backwards(self, orm):
        # Deleting field 'Recipe.photo'
        db.delete_column(u'public_recipe', 'photo')

        # Deleting field 'Recipe.directions'
        db.delete_column(u'public_recipe', 'directions')


        # Changing field 'Recipe.description'
        db.alter_column(u'public_recipe', 'description', self.gf('django.db.models.fields.CharField')(max_length=150))

    models = {
        u'public.ingredient': {
            'Meta': {'object_name': 'Ingredient'},
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['public.IngredientCategory']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'public.ingredientcategory': {
            'Meta': {'object_name': 'IngredientCategory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'public.recipe': {
            'Meta': {'object_name': 'Recipe'},
            'cook_time': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'description': ('django.db.models.fields.CharField', [], {'default': "'Yum.'", 'max_length': '200'}),
            'directions': ('django.db.models.fields.TextField', [], {'default': "'Please enter instructions on how to create this amazing cuisine.'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredients': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['public.Ingredient']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'num_servings': ('django.db.models.fields.IntegerField', [], {'max_length': '4'}),
            'photo': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'prep_time': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'tag': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['public.RecipeTag']", 'symmetrical': 'False'})
        },
        u'public.recipetag': {
            'Meta': {'object_name': 'RecipeTag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['public']