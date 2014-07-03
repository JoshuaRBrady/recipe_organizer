# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'RecipeTag'
        db.create_table(u'public_recipetag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'public', ['RecipeTag'])

        # Adding M2M table for field tag on 'Recipe'
        m2m_table_name = db.shorten_name(u'public_recipe_tag')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('recipe', models.ForeignKey(orm[u'public.recipe'], null=False)),
            ('recipetag', models.ForeignKey(orm[u'public.recipetag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['recipe_id', 'recipetag_id'])


    def backwards(self, orm):
        # Deleting model 'RecipeTag'
        db.delete_table(u'public_recipetag')

        # Removing M2M table for field tag on 'Recipe'
        db.delete_table(db.shorten_name(u'public_recipe_tag'))


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
            'tag': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['public.RecipeTag']", 'symmetrical': 'False'})
        },
        u'public.recipetag': {
            'Meta': {'object_name': 'RecipeTag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['public']