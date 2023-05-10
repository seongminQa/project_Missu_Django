from django.contrib import admin
from .models import Notice, NoticeAnswer


class NoticeAdmin(admin.ModelAdmin):
    list_display = ['title','content','category','image','created_at']
    
class NoticeAnswerAdmin(admin.ModelAdmin):
    list_display = ['author','content','created_at']

admin.site.register(Notice,NoticeAdmin)
admin.site.register(NoticeAnswer,NoticeAnswerAdmin)
