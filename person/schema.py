import graphene
from graphene import Mutation, ObjectType, ClientIDMutation
from graphene_django.types import DjangoObjectType 
from .models import Person

from rest_framework import serializers
from graphene_django.rest_framework.mutation import SerializerMutation


class PersonType(DjangoObjectType):
    class Meta:
        model = Person

# class CreatePerson(Mutation):
#     #person = graphene.Field(PersonType)

#     class Arguments:
#         name = graphene.String()
#         age = graphene.Int()

#     ok = graphene.Boolean()
#     person = graphene.Field(lambda:PersonType)

#     def mutate(self, info, name, age):
#         person = PersonType(name=name, age=age)
#         ok = True
#         return CreatePerson(person=person, ok=ok)

# 그냥 이런식으로 만들까?
class MyMutation(ObjectType):
    create_person = graphene.Field(PersonType,
                    id=graphene.Int(),
                    name=graphene.String(),
                    age=graphene.Int())
    def resolve_create_person(self, info, **kwargs):
        id=kwargs.get('id')
        name=kwargs.get('name')
        age=kwargs.get('age')
        if id is not None:
            return Person.objects.get(pk=id)
        if name is not None:
            return Person.objects.get(name=name)
        if age is not None:
            return Person.objects.get(age=age)
        return None


# class PersonSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Person
#         fields = '__all__'

# class AwesomeModelMutaion(SerializerMutation):
#     class Meta:
#         serializer_class = PersonSerializer
#         model_operations = ['create','update']
#         lookup_field = 'id'

class Query(ObjectType):
    person = graphene.Field(PersonType,
                        id=graphene.Int(),
                        name=graphene.String(),
                        age=graphene.Int())
    def resolve_person(self, info, **kwargs):
        id=kwargs.get('id')
        name=kwargs.get('name')
        age=kwargs.get('age')
        if id is not None:
            return Person.objects.get(pk=id)
        if name is not None:
            return Person.objects.get(name=name)
        if age is not None:
            return Person.objects.get(age=age)
        return None



