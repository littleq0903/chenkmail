# coding: utf-8
from django.db import models

# Create your models here.

class AbstractMember(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    
    def _get_full_name(self):
        return "%s%s" % (self.last_name, self.first_name)
    full_name = property(_get_full_name)

    def _get_email_name(self):
        return "%s <%s>"%(self._get_full_name(), self.email)
    email_name = property(_get_email_name)


    def __unicode__(self):
        return self.full_name

    class Meta:
        abstract = True
        ordering = ['last_name']


class Professor(AbstractMember):
    class Meta(AbstractMember.Meta):
        verbose_name_plural = '老師'

class TA(AbstractMember):
    class Meta(AbstractMember.Meta):
        verbose_name_plural = '助教'
