from django.db import models;
from gcharts import GChartsManager;
from Tag.models import Tag;

class Values(models.Model):


    objects = GChartsManager()

    id = models.IntegerField(db_column='idVALUES', primary_key=True, editable=False, verbose_name = 'Id')  # Field name made lowercase.
    value = models.FloatField(db_column='VALUE', verbose_name = 'Value')  # Field name made lowercase.
    datetime = models.DateTimeField(db_column='DATETIME', verbose_name = 'Date time')  # Field name made lowercase.
    tag = models.ForeignKey(Tag, db_column='tag_idTAG', verbose_name = 'Tag')  # Field name made lowercase.

    def __unicode__(self):
        return u'Tag => %s  - %s - Value => %s' % (self.tag_idtag, self.datahora, self.valor)

    class Meta:
        managed = False
        db_table = 'values'
