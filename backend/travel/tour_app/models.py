from django.db import models
from statistics import mean

class BaseTour(models.Model):
    tour_title = models.CharField(max_length=255)
    tour_overview = models.TextField()
    
    tour_category = models.ForeignKey('tour_app.TourCategory', on_delete=models.SET_NULL, related_name="tour", null=True)

    class Meta:
        abstract = True
    
class Tour(BaseTour):

    def __str__(self):
        return self.tour_title

    @property
    def get_average_rating(self):
        return mean(self.tour_review.values_list('rating', flat=True))

    @property
    def get_starting_price(self):
        return self.tour_details.values_list('price', flat=True).order_by('price')[0]

    @property
    def get_main_image(self):
        return self.tour_gallery.get(media_file_name='main').media_file.url

class TourCategory(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name

class TourJourney(models.Model):
    journey_title = models.CharField(max_length=150)
    journey_details = models.TextField()

    tour = models.ForeignKey("tour_app.tour", related_name="tour_journey", on_delete=models.CASCADE)

    def __str__(self):
        return self.journey_title

class TourGallery(models.Model):
    media_file = models.FileField(null=True, upload_to='gallery/')
    media_file_name = models.CharField(max_length=40)

    tour = models.ForeignKey('tour_app.tour', on_delete=models.CASCADE, related_name="tour_gallery")

    def __str__(self):
        return self.media_file_name

class TourMap(models.Model):
    latitude = models.CharField(max_length=25)
    longitude = models.CharField(max_length=25)
    location_name = models.CharField(max_length=15)

    tour = models.ForeignKey("tour_app.tour", related_name="tour_map", on_delete=models.CASCADE)

class TourDetails(models.Model):
    duration = models.CharField(max_length=20)
    price = models.PositiveIntegerField()

    tour = models.ForeignKey('tour_app.tour', on_delete=models.CASCADE, related_name="tour_details")

    def __str__(self):
        return str(self.pk)

class TourIncludesAndExcludes(models.Model):
    title = models.CharField(max_length=150)
    is_included = models.BooleanField()

    tour = models.ForeignKey('tour_app.tour', on_delete=models.CASCADE, related_name="tour_includes_excludes")

    def __str__(self):
        return self.title

class TourReview(models.Model):
    rating = models.PositiveSmallIntegerField()
    reviews_user = models.CharField(max_length=25)
    comment = models.TextField(blank=True)
    review_date = models.DateField(auto_now_add=True)

    tour = models.ForeignKey('tour_app.tour', on_delete=models.CASCADE, related_name="tour_review")

    def __str__(self):
        return str(self.pk)
    