from tour_app.graphql.query import *

class RootTourQuery(TourQuery):
    pass

schema = graphene.Schema(query=RootTourQuery)
