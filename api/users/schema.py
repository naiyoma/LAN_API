import graphene

from graphene_django.types import DjangoObjectType

from api.users.models import Category

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category

class Query(object):
    all_categories = graphene.List(CategoryType)

    def resolve_all_categories(self, info, **kwargs):
        return Category.objects.all()
