from django.contrib import admin
from django.utils.html import format_html

from .models import Location, Major, Subject, University


class UniversityAdmin(admin.ModelAdmin):
    filter_horizontal = ['majors', 'subjects']
    search_fields = ['title']
    list_per_page = 10

    def logo_tag(self, obj):
        return format_html('<img src="{}" height="50" />'.format(obj.logo.url))

    def wallpaper_tag(self, obj):
        try:
            url = obj.wallpaper.url
        except:
            url = ""
        return format_html('<img src="{}" height="50" />'.format(url))

    logo_tag.short_description = 'logo'
    wallpaper_tag.short_description = 'wallpaper'

    list_display = ['title', 'logo_tag', 'wallpaper_tag', 'location', 'website']

class LocationAdmin(admin.ModelAdmin):
    search_fields = ['title']

class MajorAdmin(admin.ModelAdmin):
    search_fields = ['title']

class SubjectAdmin(admin.ModelAdmin):
    search_fields = ['title']


admin.site.register(University, UniversityAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Major, MajorAdmin)
admin.site.register(Subject, SubjectAdmin)
