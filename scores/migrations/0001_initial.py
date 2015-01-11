# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Score'
        db.create_table(u'scores_score', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pst', self.gf('django.db.models.fields.IntegerField')()),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('positivePersonality', self.gf('django.db.models.fields.IntegerField')()),
            ('negativePersonality', self.gf('django.db.models.fields.IntegerField')()),
            ('positiveReviewMentions', self.gf('django.db.models.fields.IntegerField')()),
            ('negativeReviewMentions', self.gf('django.db.models.fields.IntegerField')()),
            ('userScore', self.gf('django.db.models.fields.IntegerField')()),
            ('ps', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'scores', ['Score'])


    def backwards(self, orm):
        # Deleting model 'Score'
        db.delete_table(u'scores_score')


    models = {
        u'scores.score': {
            'Meta': {'object_name': 'Score'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'negativePersonality': ('django.db.models.fields.IntegerField', [], {}),
            'negativeReviewMentions': ('django.db.models.fields.IntegerField', [], {}),
            'positivePersonality': ('django.db.models.fields.IntegerField', [], {}),
            'positiveReviewMentions': ('django.db.models.fields.IntegerField', [], {}),
            'ps': ('django.db.models.fields.IntegerField', [], {}),
            'pst': ('django.db.models.fields.IntegerField', [], {}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'userScore': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['scores']