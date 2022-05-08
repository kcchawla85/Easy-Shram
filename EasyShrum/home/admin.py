from django.contrib import admin
from .models import AdminUser, UserLabour, PostedJobs

# Register your models here.

admin.site.register(AdminUser)
admin.site.register(UserLabour)
admin.site.register(PostedJobs)