from django.contrib import admin

from .models import Contact

from .models import Hackathon

from .models import Tool


# Register your models here.

admin.site.register(Contact)

admin.site.register(Hackathon)

admin.site.register(Tool)


