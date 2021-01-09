import graphene
from graphene_django import DjangoObjectType
from tour_app.models import *
from django.conf import settings


class TourDetailsType(DjangoObjectType):
    class Meta:
        model = TourDetails

class TourReviewType(DjangoObjectType):
    class Meta:
        model = TourReview

class TourGalleryType(DjangoObjectType):
    class Meta:
        model = TourGallery
    
    media_file = graphene.String()
    def resolve_media_file(self, info):
        base_url = settings.BASE_URL
        return f"{base_url}{self.media_file.url}"

class TourType(DjangoObjectType):
    average_rating = graphene.String(source='get_average_rating')
    starting_price = graphene.String(source='get_starting_price')
    main_image = graphene.String()

    class Meta:
        model = Tour

    def resolve_main_image(self, info):
        return f"{settings.BASE_URL}{self.get_main_image}"