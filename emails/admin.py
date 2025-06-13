from django.contrib import admin

from emails.models import Email, EmailVerificationEvent

# Register your models here.

admin.site.register(Email)
admin.site.register(EmailVerificationEvent)
