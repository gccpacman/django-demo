# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Poll.pub_date'
        db.add_column('polls_poll', 'pub_date',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2015, 6, 17, 0, 0)),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Poll.pub_date'
        db.delete_column('polls_poll', 'pub_date')


    models = {
        'polls.poll': {
            'Meta': {'object_name': 'Poll'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['polls']