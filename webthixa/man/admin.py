from django.contrib import admin
from .models import Conference, Nameplate, Category, Element
# Register your models here.

admin.site.register(Conference)
admin.site.register(Nameplate)
admin.site.register(Category)
admin.site.register(Element)
