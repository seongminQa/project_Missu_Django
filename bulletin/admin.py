from django.contrib import admin
from .models import Bulletin, BulletinAnswer


class BulletinAdmin(admin.ModelAdmin):
    list_display = ['title','author','content','image','created_at']
    
class BulletinAnswerAdmin(admin.ModelAdmin):
    list_display = ['author','content','image','created_at']

admin.site.register(Bulletin,BulletinAdmin)
admin.site.register(BulletinAnswer,BulletinAnswerAdmin)
