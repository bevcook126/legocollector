from django.contrib import admin
from .models import Lego, Minifig, Collection, Photo

# Register your models here.

admin.site.register(Lego)
admin.site.register(Minifig)
admin.site.register(Collection)
admin.site.register(Photo)