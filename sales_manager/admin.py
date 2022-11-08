from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Movement, Dividend, Invoice, Manager
from .forms import UserAdmin


admin.site.register(Dividend, UserAdmin)
admin.site.register(Movement)
admin.site.register(Invoice)

admin.site.unregister(Group)