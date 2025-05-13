from django.contrib import admin
from .models import User, TrustedContact

admin.site.register(User)
admin.site.register(TrustedContact)
