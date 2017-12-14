from django.contrib import admin
from .models import Profile, Rant, Reaction

# Register your models here.

admin.site.register(Profile)
admin.site.register(Rant)
admin.site.register(Reaction)


