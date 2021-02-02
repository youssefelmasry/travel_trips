from users.graphql.schema import UserMutation, graphene, UserQuery
from tour_app.graphql.schema import TourQuery, TourMutation

class RootMutation(UserMutation, TourMutation):
    pass

class RootQuery(TourQuery, UserQuery):
    pass

schema = graphene.Schema(query=RootQuery, mutation=RootMutation)
