# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import User, Company, Domain, Domain_stats


# Register your models here.

admin.site.register(User)
admin.site.register(Company)
admin.site.register(Domain)
admin.site.register(Domain_stats)
