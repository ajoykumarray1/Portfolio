from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(About)
admin.site.register(Service)
admin.site.register(RecentWork)
admin.site.register(Client)