from django.contrib import admin
from . models import SentEmail


@admin.register(SentEmail)
class EmailDisplay(admin.ModelAdmin):
    list_display = ['subject','to_email','message','is_opened','sent_at']
    list_display_links = ['subject','to_email','message','sent_at']
