from django.contrib import admin
from .models import Debate, Comments


class InfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'like_count',)
    def like_count(self,obj):
        return obj.likes.all().count()

# Register your models here.
admin.site.register(Debate, InfoAdmin)
admin.site.register(Comments)