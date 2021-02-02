from django.contrib.auth import get_user_model
from graphene_django import DjangoObjectType
import graphql_jwt
import graphene
import graphql_social_auth
from graphql_jwt.decorators import login_required
from django.conf import settings

class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()
        fields = ['id', 'email', 'first_name', 'last_name', 'photo']

    def resolve_photo(self, info):
        return f"{settings.BASE_URL}{self.photo.url}"

class UserQuery(graphene.ObjectType):
    user_obj = graphene.Field(UserType)

    @login_required
    def resolve_user_obj(self, info):
        return info.context.user

class CreateUser(graphene.Mutation):
    user = graphene.String()

    class Arguments:
        password = graphene.String(required=True)
        email = graphene.String(required=True)
        first_name = graphene.String(required=False)
        last_name = graphene.String(required=False)

    def mutate(self, info, password, email, first_name=None, last_name=None):
        photo = info.context.FILES.get('profileimage', None)

        user = get_user_model()(
            email=email,
            first_name=first_name,
            last_name=last_name,
            photo=photo
        )
        user.set_password(password)
        user.save()

        return CreateUser(user=user.email)

class UserMutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    revoke_token = graphql_jwt.Revoke.Field()
    social_auth = graphql_social_auth.SocialAuthJWT.Field()
    create_user = CreateUser.Field()