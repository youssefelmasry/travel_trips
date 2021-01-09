from django.contrib import admin
from tour_app.models import *
from django.utils.safestring import mark_safe
from django.urls import reverse

class TourGalleryInline(admin.TabularInline):
    model = TourGallery
    extra = 1

class TourJourneyInline(admin.TabularInline):
    model = TourJourney
    extra = 1

class TourReviewInline(admin.TabularInline):
    model = TourReview
    extra = 1

class TourMapInline(admin.TabularInline):
    model = TourMap
    extra = 1

class TourIncludesAndExcludesInline(admin.TabularInline):
    model = TourIncludesAndExcludes
    extra = 1

class TourDetailsInline(admin.TabularInline):
    model = TourDetails
    extra = 1

@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ['tour_title', 'tour_overview', 'tour_category']
    list_filter = ['tour_category__category_name']
    inlines = [TourDetailsInline, TourGalleryInline, TourJourneyInline, TourIncludesAndExcludesInline, TourMapInline, TourReviewInline]

@admin.register(TourJourney)
class TourJourneyAdmin(admin.ModelAdmin):
    list_display = ['journey_title', 'tour_link']
    list_filter = ['tour__tour_title']

    def tour_link(self, tourobj):
        url = reverse("admin:tour_app_tour_change", args=[tourobj.tour.id])
        link = '<a href="%s">%s</a>' % (url, tourobj.tour.tour_title)
        return mark_safe(link)
    tour_link.short_description = 'Tour'

@admin.register(TourDetails)
class TourDetailsAdmin(admin.ModelAdmin):
    list_display = ['duration', 'price', 'tour_link']
    list_filter = ['tour__tour_title']

    def tour_link(self, tourobj):
        url = reverse("admin:tour_app_tour_change", args=[tourobj.tour.id])
        link = '<a href="%s">%s</a>' % (url, tourobj.tour.tour_title)
        return mark_safe(link)
    tour_link.short_description = 'Tour'


admin.register(TourMap)
class TourMapAdmin(admin.ModelAdmin):
    list_display = ['latitude', 'longitude', 'location_name', 'tour_link']
    list_filter = ['tour__tour_title']
    
    def tour_link(self, tourobj):
        url = reverse("admin:tour_app_tour_change", args=[tourobj.tour.id])
        link = '<a href="%s">%s</a>' % (url, tourobj.tour.tour_title)
        return mark_safe(link)
    tour_link.short_description = 'Tour'

admin.site.register(TourReview)
admin.site.register(TourIncludesAndExcludes)
admin.site.register(TourCategory)