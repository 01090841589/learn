from django.contrib import admin

# Register your models here.
class JobAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'past_job',)