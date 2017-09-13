from graphene import relay, ObjectType, AbstractType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from theseus.organizations.models import Company


# Graphene will automatically map the Category model's fields onto the CategoryNode.
# This is configured in the CategoryNode's Meta class (as you can see below)
class CompanyNode(DjangoObjectType):
    class Meta:
        model = Company
        filter_fields = ['name', 'created_at', 'updated_at', 'created_by_user']
        interfaces = (relay.Node, )


class Query(AbstractType):
    company = relay.Node.Field(CompanyNode)
    all_companies = DjangoFilterConnectionField(CompanyNode)
