from django.contrib import admin
from services.models import oneServices, accardionServices


class accardionServicesInline(admin.TabularInline):
	model = accardionServices
	extra = 1

@admin.register(oneServices)
class oneServicesAdmin(admin.ModelAdmin):
	list_display = ["titleServices", "directionServices", "imgServices"]
	inlines = [accardionServicesInline]
	fields = [("titleServices", "directionServices"), ("imgServices","descriptionServices"), "textServices", ("videoServices", "imgVideoServices"), "titleQveschenServices"]
