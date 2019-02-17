import graphene
import cookbook.schema
import animal.schema
import person.schema

class Query(cookbook.schema.Query, animal.schema.Query, person.schema.Query, graphene.ObjectType):
    pass
class Mutation(person.schema.MyMutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query
                    , mutation=Mutation
                    )