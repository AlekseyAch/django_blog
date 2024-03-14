from django.contrib import admin
from .models import ContactsModal, ContactInfo, socialLinks, hiroBlock, galleryHomePage, ourAwards, WorkStepsHomePage, OneStepHomePage, footerInfo, polysiFooter

@admin.register(ContactsModal)
class ContactsModalAdmin(admin.ModelAdmin):
	list_display = ["id", "name", "email", "create_add"]
	list_display_links = ("name",)

@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
	list_display = ["title_block", "phone", "email_site", "adress_local"]

@admin.register(socialLinks)
class socialLinksAdmin(admin.ModelAdmin):
	list_display = ["ikons", "link"]


class GalleryInline(admin.TabularInline):
    model = galleryHomePage
    extra = 1

@admin.register(hiroBlock)
class HiroBlockAdmin(admin.ModelAdmin):
    list_display = ["h1_site", "image"]
    inlines = [GalleryInline]

@admin.register(ourAwards)
class ourAwardsAdmin(admin.ModelAdmin):
	list_display = ["title", "text", "yar"]

class OneStepInline(admin.TabularInline):
    model = OneStepHomePage
    extra = 1

@admin.register(WorkStepsHomePage)
class WorkStepsHomePageAdmin(admin.ModelAdmin):
	list_display = ["TitleWorkSteps"]
	inlines = [OneStepInline]

class polysiFooterInline(admin.TabularInline):
	model = polysiFooter
	extra = 1


@admin.register(footerInfo)
class footerInfoAdmin(admin.ModelAdmin):
	list_display = ["bigText"]
	inlines = [polysiFooterInline]