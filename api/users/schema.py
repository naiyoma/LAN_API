import graphene

from graphene_django.types import DjangoObjectType

from api.users.models import User

class User(DjangoObjectType):
    class Meta:
        model = User

class Query(graphene.ObjectType):
    users = graphene.List(User)

    def resolve_users(self, info):
        return UserModel.objects.all()
