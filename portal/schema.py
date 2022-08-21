import graphene
from portal.apps.courses import schema as course_schema


class Query(course_schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
