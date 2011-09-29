#!/usr/bin/env python
# encoding=utf-8
# maintainer: Fad

import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy, ugettext as _


class Download(models.Model):
    """ """
    LEVEL_URGENT = "f"
    LEVEL_DEFAULT = "n"
    LEVEL_SLOW = "s"
    LEVEL = ((LEVEL_URGENT, u"urgent"), (LEVEL_DEFAULT, u"default"), \
              (LEVEL_SLOW, u"Slow"))
    URL = "u"
    TORRENTE = "T"
    TYPE = ((URL, u"url"), (TORRENTE, u"Torrente"))
    START = "c"
    PAUSE = "p"
    STOP = "a"
    STATUS = ((START, u"start"), (PAUSE, u"pause"), (STOP, u"stop"))
    types = models.CharField(max_length=30, verbose_name=(_("type")),\
                                              choices=TYPE, default=URL)
    link = models.CharField(max_length=150,\
                            verbose_name=(_("url")))
    priority = models.CharField(max_length=30, verbose_name=(_("priority")),\
                                    choices=LEVEL, default=LEVEL_DEFAULT)
    owner = models.ForeignKey(User, related_name=_('owner'),\
                                    verbose_name=_("owner"))
    date = models.DateTimeField(verbose_name=(_("made the ")),\
                                         default=datetime.datetime.today)
    size = models.PositiveIntegerField(blank=True, \
                                       verbose_name=(_("size")))
    status = models.CharField(max_length=30, verbose_name=(_("status")),\
                                            choices=STATUS, default=START)
    path = models.CharField(max_length=250, verbose_name=(_("path")))
    progression = models.CharField(max_length=150,\
                            verbose_name=(_("progression")))

    def __unicode__(self):
        return (u'%(name)s %(priority)s %(size)d %(date)s') % \
                {"name": self.owner.username, "priority": self.priority, \
                 "size": self.size, "date": self.date}
