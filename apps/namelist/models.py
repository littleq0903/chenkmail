# coding: utf-8
from django.db import models

# Create your models here.

class AbstractMember(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    
    def _get_full_name(self):
        return "%S%S" % (self.last_name, self.first_name)

    full_name = property(_get_full_name)


    def __unicode__(self):
        return self.full_name

    class Meta:
        abstract = True
        ordering = ['last_name']


class Sendor(AbstractMember):
    class Meta:
        verbose_name_plural = '寄件人'

class Receiver(AbstractMember):
    class Meta:
        verbose_name_plural = '收件人'
