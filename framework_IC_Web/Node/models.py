from django.db import models;
from gcharts import GChartsManager;

class Node(models.Model):

    objects = GChartsManager()

    id = models.IntegerField(db_column='idSITE', primary_key=True, editable=False, verbose_name = 'Id')  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=45, verbose_name = 'Name')  # Field name made lowercase.
    information = models.CharField(db_column='INFORMATION', max_length=45, blank=True, verbose_name = 'Details')  # Field name made lowercase.

    def __unicode__(self):
        return u'%s' % (self.name)

    class Meta:
        managed = False
        db_table = 'site'
