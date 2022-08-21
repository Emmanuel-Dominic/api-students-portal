import graphene
from portal.apps.users import schema as user_schema
from portal.apps.courses import schema as course_schema


class Query(user_schema.Query, course_schema.Query, graphene.ObjectType):
    pass


class Mutation(user_schema.Mutation, course_schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
