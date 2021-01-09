from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Kwic

# Register your models here.


class KwicAdmin(admin.ModelAdmin):
    list_display = ('content', 'result')
    search_fields = ('content', 'result')
    list_filter = ('content', 'result')

admin.site.register(Kwic, KwicAdmin)