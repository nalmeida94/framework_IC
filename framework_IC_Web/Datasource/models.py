from django.db import models;
from gcharts import GChartsManager;
from Node.models import Node;


class Datasource(models.Model):

    objects = GChartsManager()

    id = models.IntegerField(db_column='idDATASOURCE', primary_key=True, editable=False, verbose_name = 'Id')  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=45, verbose_name = 'Name')  # Field name made lowercase.
    manufacturer = models.CharField(db_column='MANUFACTURER', max_length=45, blank=True, verbose_name = 'Manufacturer')  # Field name made lowercase.
    model = models.CharField(db_column='MODEL', max_length=45, blank=True, verbose_name = 'Model')  # Field name made lowercase.
    node = models.ForeignKey(Node, db_column='site_idSITE', blank=True, null=True, verbose_name = 'Node')  # Field name made lowercase.

    def __unicode__(self):
        return u' %s  - from %s' % (self.name, self.manufacturer)

    class Meta:
        managed = False
        db_table = 'datasource'
