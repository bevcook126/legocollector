from django.contrib import admin
from .models import Lego, Figure, Collection

# Register your models here.

admin.site.register(Lego)
admin.site.register(Figure)
admin.site.register(Collection)