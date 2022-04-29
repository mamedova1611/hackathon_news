from django.contrib import admin

# Register your models here.
from .models import Predpriyatie, Tag, News, Comment


class PredpriyatieAdmin(admin.ModelAdmin):
    list_display = ['bin_id', 'full_name', 'address', 'fio_ruk', 'phone']
    search_fields = ['bin_id', 'full_name']


class NewsAdmin(admin.ModelAdmin):
    list_display = ['bin_news', 'title', 'tags']

class CommentAdmin(admin.ModelAdmin):
    def get_text(self, obj):
        return obj.text[:15] + '...'

    list_display = ['username', 'get_text']

class TagsAdmin(admin.ModelAdmin):
    list_display = ['tag']

admin.site.register(Predpriyatie, PredpriyatieAdmin)
admin.site.register(Tag, TagsAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Comment, CommentAdmin)
