from .types import *

class TourQuery(graphene.ObjectType):
    all_tours = graphene.List(TourType, operation=graphene.String(), value=graphene.Int(),
                                limit=graphene.Int(default_value=None), offset=graphene.Int(default_value=None))
    tour_obj = graphene.Field(TourType, tour_id=graphene.Int())

    def resolve_all_tours(self, info, limit=None, offset=None, **kwargs):
        if 'operation' in kwargs:
            if kwargs['operation'] == 'gt':
                return Tour.objects.filter(tour_details__price__gt=kwargs['value'])
            if kwargs['operation'] == 'gte':
                return Tour.objects.filter(tour_details__price__gte=kwargs['value'])
            if kwargs['operation'] == 'lt':
                return Tour.objects.filter(tour_details__price__lt=kwargs['value'])
            if kwargs['operation'] == 'lte':
                return Tour.objects.filter(tour_details__price__lte=kwargs['value'])

        return Tour.objects.all()[offset:limit]

    def resolve_tour_obj(self, info, tour_id=None):
        return Tour.objects.get(id=tour_id)