import graphene
from graphene import relay, ObjectType
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from cookbook.models import Category, Ingredient

# Type 1
# class CategoryType(DjangoObjectType):
#     class Meta:
#         model = Category
# class IngredientType(DjangoObjectType):
#     class Meta:
#         model = Ingredient
# Type 2
class CategoryNode(DjangoObjectType):
    class Meta:
        model = Category
        filter_fields = ['name', 'ingredients']
        interfaces = (relay.Node,) 
        # 이런식으로 설정하면 name 과 ingredients 가 node(분기) 가 되는듯 하다

class IngredientNode(DjangoObjectType):
    class Meta:
        model = Ingredient
        # exact 정확 / icontains 포함 %XX% / istartswith ~시작 XX%
        # 앞에 i 가 붙으면 대소문자 구분이 없는듯 하다
        filter_fields = { 
            'name':['exact','icontains','istartswith'],
            'notes':['exact','icontains'],
            'category':['exact'],
            'category__name':['exact'], # 여기 언더바 두번이다 조심
        }
        interfaces = (relay.Node,)
# Type 2
class Query(ObjectType):
# Type 1
#class Query(Object):
    # category = graphene.Field(CategoryType, # 이건 graphene.object {CategoryType : {id : int, name : string}}
    #                     id=graphene.Int(),
    #                     name=graphene.String())
    # all_categories = graphene.List(CategoryType) # 이건 graphene.array [CategoryType] 이란 뜻으로 / [models.Category]
    # ingredient = graphene.Field(IngredientType, # 이건 graphene.object {IngredientType : {id : int, name : string}}
    #                     id=graphene.Int(),
    #                     name=graphene.String())
    # all_ingredients = graphene.List(IngredientType) # 이건 graphene.array [IngredientType] 이란 뜻으로 / [models.Ingredient]
    # 위의 query 와 아래 resolve 는 매칭되는 방식
    # query 의 변수가 타입 선언이라고 보면 되고, 아래 resolve 가 조건 이라고 보면 된다.
    # def resolve_all_categories(self, info, **kwargs):
    #     return Category.objects.all()
    # def resolve_all_ingredients(self, info, **kwargs):
    #     return Ingredient.objects.select_related('category').all()
    # def resolve_category(self, info, **kwargs):
    #     id=kwargs.get('id')
    #     name=kwargs.get('name')
    #     if id is not None:
    #         return Category.objects.get(pk=id)
    #     if name is not None:
    #         return Category.objects.get(name=name)
    #     return None
    # def resolve_ingredient(self, info, **kwargs):
    #     id=kwargs.get('id')
    #     name=kwargs.get('name')
    #     if id is not None:
    #         return Ingredient.objects.get(pk=id)
    #     if name is not None:
    #         return Ingredient.objects.get(name=name)
    #     return None

    # Type 2
    # category 와 ingredient 에는 id 값으로 밖에 접근이 안되는듯 하다
    category = relay.Node.Field(CategoryNode)
    all_categories = DjangoFilterConnectionField(CategoryNode)
    ingredient = relay.Node.Field(IngredientNode)
    all_ingredients = DjangoFilterConnectionField(IngredientNode)
