# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Tournament'
        db.create_table(u'tournaments_tournament', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=254)),
            ('start', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('end', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'tournaments', ['Tournament'])

        # Adding model 'Team'
        db.create_table(u'tournaments_team', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tournament', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tournaments.Tournament'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('members', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'tournaments', ['Team'])

        # Adding model 'Match'
        db.create_table(u'tournaments_match', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tournament', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tournaments.Tournament'])),
            ('team1', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['tournaments.Team'])),
            ('team2', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['tournaments.Team'])),
            ('map_name', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('start', self.gf('django.db.models.fields.DateTimeField')()),
            ('points_team1', self.gf('django.db.models.fields.SmallIntegerField')(null=True, blank=True)),
            ('points_team2', self.gf('django.db.models.fields.SmallIntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'tournaments', ['Match'])


    def backwards(self, orm):
        # Deleting model 'Tournament'
        db.delete_table(u'tournaments_tournament')

        # Deleting model 'Team'
        db.delete_table(u'tournaments_team')

        # Deleting model 'Match'
        db.delete_table(u'tournaments_match')


    models = {
        u'tournaments.match': {
            'Meta': {'object_name': 'Match'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'map_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'points_team1': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'points_team2': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'start': ('django.db.models.fields.DateTimeField', [], {}),
            'team1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['tournaments.Team']"}),
            'team2': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['tournaments.Team']"}),
            'tournament': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tournaments.Tournament']"})
        },
        u'tournaments.team': {
            'Meta': {'object_name': 'Team'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'members': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'tournament': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tournaments.Tournament']"})
        },
        u'tournaments.tournament': {
            'Meta': {'object_name': 'Tournament'},
            'end': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            'start': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['tournaments']