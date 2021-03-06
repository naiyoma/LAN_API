import graphene

from graphene_django.types import DjangoObjectType
# from graphene_django.filter import DjangoFilterConnectionField

from.models import User, Category

class UserType(DjangoObjectType):
    class Meta:
        model = User

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category

class Query(graphene.ObjectType):
    category = graphene.Field(CategoryType,
                            id=graphene.Int(),
                            name=graphene.String())
    users = graphene.Field(UserType,
                           id=graphene.Int(),
                           name=graphene.String())
    all_users = graphene.List(UserType)
    all_categories = graphene.List(CategoryType)

    def resolve_category(self, info, **kwargs):
        #fetching a single category based on name
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return Category.objects.get(pk=id)

        if name is not None:
            return Category.objects.get(name=name)

        return None

    def resolve_user(self, info, **kwargs):
        #fetching a single user
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return User.objects.get(pk=id)

        if name is not None:
            return User.objects.get(name=name)

        return None

    def resolve_all_users(self, info, **Kwargs):
        """
        fetching all users.
        """
        return User.objects.all()

    def resolve_all_categories(self, info, **Kwargs):
        """
        fetching all categories.
        """
        return Category.objects.all()

schema = graphene.Schema(query=Query)
