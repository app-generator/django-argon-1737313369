# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    fb_user = models.TextField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Pack(models.Model):

    #__Pack_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)
    created = models.DateTimeField(blank=True, null=True, default=timezone.now)
    updated = models.DateTimeField(blank=True, null=True, default=timezone.now)
    available = models.BooleanField()

    #__Pack_FIELDS__END

    class Meta:
        verbose_name        = _("Pack")
        verbose_name_plural = _("Pack")


class Item(models.Model):

    #__Item_FIELDS__
    available = models.BooleanField()

    #__Item_FIELDS__END

    class Meta:
        verbose_name        = _("Item")
        verbose_name_plural = _("Item")



#__MODELS__END
