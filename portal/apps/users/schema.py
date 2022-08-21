import graphene
from .types import User
from django.contrib.auth.models import User as UserModel


class Query(graphene.ObjectType):
    users = graphene.List(User)
    user = graphene.Field(User, user_id=graphene.Int())

    def resolve_users(self, info, **kwargs):
        return UserModel.objects.all().order_by('id')

    def resolve_user(self, info, user_id):
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None
