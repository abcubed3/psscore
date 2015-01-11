# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PublicServant'
        db.create_table(u'publicservants_publicservant', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('firstName', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=60, null=True, blank=True)),
            ('middleName', self.gf('django.db.models.fields.CharField')(max_length=120, null=True, blank=True)),
            ('lastName', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('currentPosition', self.gf('django.db.models.fields.CharField')(max_length=120, null=True, blank=True)),
            ('formerPosition', self.gf('django.db.models.fields.CharField')(max_length=120, null=True, blank=True)),
            ('department', self.gf('django.db.models.fields.CharField')(max_length=120, null=True, blank=True)),
            ('ministry', self.gf('django.db.models.fields.CharField')(max_length=120, null=True, blank=True)),
            ('startAtMinistry', self.gf('django.db.models.fields.DateField')(null=True)),
            ('endAtMinistry', self.gf('django.db.models.fields.DateField')(null=True)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_Timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'publicservants', ['PublicServant'])


    def backwards(self, orm):
        # Deleting model 'PublicServant'
        db.delete_table(u'publicservants_publicservant')


    models = {
        u'publicservants.publicservant': {
            'Meta': {'object_name': 'PublicServant'},
            'currentPosition': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'department': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'endAtMinistry': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'firstName': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'formerPosition': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastName': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'middleName': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'ministry': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'startAtMinistry': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'updated_Timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['publicservants']