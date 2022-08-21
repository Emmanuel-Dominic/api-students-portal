from graphene_django import DjangoObjectType
from .models import Course as CourseModel
from graphene.types.scalars import Scalar


class Course(DjangoObjectType):
    class Meta:
        model = CourseModel


class ObjectField(Scalar):  # to serialize error message from serializer
    @staticmethod
    def serialize(dt):
        return dt
