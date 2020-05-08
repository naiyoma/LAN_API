import graphene

import api.users.schema

class Query(api.users.schema.Query, graphene.ObjectType):
    #This will inherit from multiple Queries
    pass
schema = graphene.Schema(query=Query)
