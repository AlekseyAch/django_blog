from django.contrib import admin
from services.models import oneServices, accardionServices


class accardionServicesInline(admin.TabularInline):
	model = accardionServices
	extra = 1

@admin.register(oneServices)
class oneServicesAdmin(admin.ModelAdmin):
	list_display = ["titleServices", "directionServices", "imgServices", "sortNumber"]
	inlines = [accardionServicesInline]
	fields = [("titleServices", "directionServices", "sortNumber", "slug"), ("imgServices","descriptionServices"), "textServices", ("videoServices", "imgVideoServices"), "titleQveschenServices"]
	prepopulated_fields = {'slug': ('titleServices',)}
