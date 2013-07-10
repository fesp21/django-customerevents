# -*- coding: utf-8 -*-
from django.db import models
from jsonfield import JSONField


class Customer(models.Model):
    identity = models.CharField(max_length=256, unique=True)
    properties = JSONField(blank=True)
    active = models.BooleanField(default=True, db_index=True)

    def __unicode__(self):
        return self.identity

class Alias(models.Model):
    customer = models.ForeignKey(Customer, related_name='aliases')
    identity = models.CharField(max_length=256, unique=True)

    def __unicode__(self):
        return self.identity

class Event(models.Model):
    customer = models.ForeignKey(Customer, related_name='events')
    name = models.CharField(max_length=256)
    timestamp = models.DateTimeField(auto_now_add=True)
    properties = JSONField(blank=True)

    def __unicode__(self):
        return self.name