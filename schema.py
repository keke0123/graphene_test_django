import graphene
import cookbook.schema
import animal.schema

class Query(cookbook.schema.Query, animal.schema.Query, graphene.ObjectType):
    pass
schema = graphene.Schema(query=Query)