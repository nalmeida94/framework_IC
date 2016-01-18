from django.db import models;
from gcharts import GChartsManager;
from Datasource.models import Datasource;


class Radio(models.Model):

    objects = GChartsManager()

    id = models.IntegerField(db_column='idRADIO', primary_key=True, editable=False, verbose_name = 'Id')
    endreal = models.CharField(db_column='ENDREAL', max_length=64, blank=True, verbose_name = 'Full address')  # Field name made lowercase.
    radioInfo = models.ForeignKey('RadioInfo', db_column='radioInfo_idRADIOINFO', verbose_name = "Radio's Type")  # Field name made lowercase.
    datasource = models.ForeignKey(Datasource, db_column='datasource_idDATASOURCE', blank=True, null=True, verbose_name = 'Datasource')  # Field name made lowercase.

    def __unicode__(self):
        return u'datasource = %s  / type = %s' % (self.datasource_id, self.radioInfo)

    class Meta:
        managed = False
        db_table = 'radio'


class RadioInfo(models.Model):

    objects = GChartsManager()

    id = models.IntegerField(db_column='idRADIOINFO', primary_key=True, editable=False, verbose_name = 'Id')  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=45, verbose_name = 'Name')
    description = models.CharField(db_column='DESCRIPTION', max_length=300, blank=True, verbose_name = 'Details')

    def __unicode__(self):
        return u'name = %s  / description = %s' % (self.name, self.description)

    class Meta:
        managed = False
        db_table = 'radioinfo'
