from django.contrib import admin
from .models import Movement, Dividend, Invoice

admin.site.register(Movement)
admin.site.register(Dividend)
admin.site.register(Invoice)