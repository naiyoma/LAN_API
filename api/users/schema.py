import graphene

from graphene_django.types import DjangoObjectType

from.models import User, Category

class UserType(DjangoObjectType):
    class Meta:
        model = User

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category

class Query(graphene.ObjectType):
    all_users = graphene.List(UserType)
    all_categories = graphene.List(CategoryType)

    def resolve_users(self, info, **Kwargs):
        return User.objects.all()

    def resolve_all_categories(self, info, **Kwargs):
        return Category.objects.all()

schema = graphene.Schema(query=Query)
