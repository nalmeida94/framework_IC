from django.db import models;
from gcharts import GChartsManager;
from Tag.models import Tag;

class Snapshot(models.Model):

    objects = GChartsManager()

    id = models.IntegerField(db_column='idSNAP', primary_key=True, editable=False, verbose_name = 'Id')  # Field name made lowercase.
    value = models.FloatField(db_column='VALUE', verbose_name = 'Value')  # Field name made lowercase.
    snapshot = models.DateTimeField(db_column='SNAPSHOT', verbose_name = 'Snapshot')  # Field name made lowercase.
    tag = models.ForeignKey(Tag, db_column='tag_idTAG', verbose_name = 'Tag')  # Field name made lowercase.

    def __unicode__(self):
        return u'tag = %s  / value = %s' % (self.tag_id, self.value)

    class Meta:
        managed = False
        db_table = 'snapshot'
