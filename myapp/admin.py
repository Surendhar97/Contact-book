from django.contrib import admin
from .models import Yellowpages

class YellowpagesAdmin(admin.ModelAdmin):
    list_display=("FirstName","LastName","City","ContactNumber")
admin.site.register(Yellowpages,YellowpagesAdmin)