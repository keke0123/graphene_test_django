import graphene
from graphene import relay, ObjectType
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from animal.models import Animal

class AnimalNode(DjangoObjectType):
    class Meta:
        model = Animal
        filter_fields = ['name','genus','is_domesticated']
        # only_fields / exclude_fields 도 있다.
        interfaces = (relay.Node,)
class Query(ObjectType):
    animal = relay.Node.Field(AnimalNode)
    all_animal = DjangoFilterConnectionField(AnimalNode)



