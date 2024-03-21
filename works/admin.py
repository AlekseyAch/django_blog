from django.contrib import admin
from .models import works, WorksGallery, WorksCategory, WorksGallery
from mptt.admin import MPTTModelAdmin


class WorksGalleryInline(admin.TabularInline):
	model = WorksGallery
	extra = 2

@admin.register(works)
class worksAdmin(admin.ModelAdmin):
	list_display = ["titleWorks"]
	prepopulated_fields = ({'slug': ('titleWorks',)})
	inlines = [WorksGalleryInline]


admin.site.register(WorksCategory, MPTTModelAdmin)
class WorksCategoryAdmin(admin.ModelAdmin):
	list_display = ["WorksCategoryItem"]
	fields = ["WorksCategoryItem", "slug", "parent"]
	prepopulated_fields = ({'slug': ('WorksCategoryItem',)})


