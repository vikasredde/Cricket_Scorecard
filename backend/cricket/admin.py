from django.contrib import admin
from . import models



admin.site.register(models.Team)
admin.site.register(models.Player)
admin.site.register(models.Match)
admin.site.register(models.Innings)
admin.site.register(models.Ball)

