from django.db import models;
from gcharts import GChartsManager;
from Datasource.models import Datasource;

class Tag(models.Model):

    objects = GChartsManager()

    id = models.IntegerField(db_column='idTAG', primary_key=True, editable=False, verbose_name = 'Id')  # Field name made lowercase.
    diversion = models.FloatField(db_column='DEVIATION', blank=True, null=True, verbose_name = 'Diversion')  # Field name made lowercase.
    max_time = models.IntegerField(db_column='TIME_MAX', blank=True, null=True, verbose_name = 'Max time')  # Field name made lowercase.
    conv_rate = models.IntegerField(db_column='CONV_RATE', blank=True, null=True, verbose_name = 'Convertion rate')  # Field name made lowercase.
    channel = models.PositiveIntegerField(db_column='CHANNEL', blank=True, null=True, verbose_name = 'Channel')
    tagInfo = models.ForeignKey('TagInfo', db_column='tagInfo_idTAGINFO', verbose_name = 'Tag Info')  # Field name made lowercase.
    datasource = models.ForeignKey(Datasource, db_column='datasource_idDATASOURCE', blank=True, null=True, verbose_name = 'Datasource')  # Field name made lowercase.

    def __unicode__(self):
        return u'id => %s - id tag information => %s' % (self.id, self.tagInfo)

    class Meta:
        managed = False
        db_table = 'tag'


class TagInfo(models.Model):

    objects = GChartsManager()

    id = models.IntegerField(db_column='idTAGINFO', primary_key=True, editable=False, verbose_name = 'Id')  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=45, verbose_name = 'Name')  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=255, blank=True, verbose_name = 'Details')  # Field name made lowercase.

    def __unicode__(self):
        return u'%s. Description: %s' % (self.name, self.description)

    class Meta:
        managed = False
        db_table = 'taginfo'
