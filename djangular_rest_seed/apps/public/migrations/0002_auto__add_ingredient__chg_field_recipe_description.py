# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Ingredient'
        db.create_table(u'public_ingredient', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'public', ['Ingredient'])

        # Adding M2M table for field ingredient on 'Recipe'
        m2m_table_name = db.shorten_name(u'public_recipe_ingredient')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('recipe', models.ForeignKey(orm[u'public.recipe'], null=False)),
            ('ingredient', models.ForeignKey(orm[u'public.ingredient'], null=False))
        ))
        db.create_unique(m2m_table_name, ['recipe_id', 'ingredient_id'])


        # Changing field 'Recipe.description'
        db.alter_column(u'public_recipe', 'description', self.gf('django.db.models.fields.CharField')(max_length=150))

    def backwards(self, orm):
        # Deleting model 'Ingredient'
        db.delete_table(u'public_ingredient')

        # Removing M2M table for field ingredient on 'Recipe'
        db.delete_table(db.shorten_name(u'public_recipe_ingredient'))


        # Changing field 'Recipe.description'
        db.alter_column(u'public_recipe', 'description', self.gf('django.db.models.fields.CharField')(max_length=100))

    models = {
        u'public.ingredient': {
            'Meta': {'object_name': 'Ingredient'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'public.recipe': {
            'Meta': {'object_name': 'Recipe'},
            'description': ('django.db.models.fields.CharField', [], {'default': "'No description has be entered.'", 'max_length': '150'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredient': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['public.Ingredient']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['public']