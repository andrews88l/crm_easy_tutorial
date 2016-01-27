from django.contrib import admin
from .models import Communication

# Register your models here.

class CommunicationAdmin(admin.ModelAdmin):
	list_display = ('subject', 'uuid')

admin.site.register(Communication, CommunicationAdmin)