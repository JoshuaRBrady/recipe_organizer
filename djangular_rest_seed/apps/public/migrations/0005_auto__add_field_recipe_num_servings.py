# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Recipe.num_servings'
        db.add_column(u'public_recipe', 'num_servings',
                      self.gf('django.db.models.fields.IntegerField')(default=1, max_length=4),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Recipe.num_servings'
        db.delete_column(u'public_recipe', 'num_servings')


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
            'description': ('django.db.models.fields.CharField', [], {'default': "'Yum.'", 'max_length': '150'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredients': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['public.Ingredient']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'num_servings': ('django.db.models.fields.IntegerField', [], {'max_length': '4'}),
            'tag': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['public.RecipeTag']", 'symmetrical': 'False'})
        },
        u'public.recipetag': {
            'Meta': {'object_name': 'RecipeTag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['public']