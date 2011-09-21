#!/usr/bin/env python
# encoding=utf-8
# maintainer: Fad

import datetime
from django.db import models
from django.contrib.auth.models import User


class Owner(User):
    
    phone = models.CharField(max_length=30, blank=True,
                                verbose_name=("Telephone"))

    def __unicode__(self):
        return _(u'%(name)s') % {"name": self.username}


class Download(models.Model):
    """ """
    LEVEL_FAST = "f"
    LEVEL_NOR = "n"
    LEVEL_SLOW = "s"
    LEVEL = (
        (LEVEL_FAST, u"Fast"),
        (LEVEL_NOR, u"Normal"),
        (LEVEL_SLOW, u"Slow")
    )
    link_download = models.CharField(max_length=150,\
                            verbose_name=("url"))
    priority =  models.CharField(max_length=30,
                            verbose_name=("priority"),\
                            choices=LEVEL, default=LEVEL_NOR)
    owner = models.ForeignKey(Owner, related_name='owner',\
                                     verbose_name=("priority"))
