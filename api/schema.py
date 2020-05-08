import graphene

import api.users.schema

class Query(api.users.schema.Query, graphene.ObjectType):
    #This class will inherit from multiple Queries
    # this will include all the apps that have been created
    pass

schema = graphene.Schema(query=Query)
