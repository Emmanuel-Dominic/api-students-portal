import graphene
from .types import Course
from .models import Course as CourseModel


class Query(graphene.ObjectType):
    courses = graphene.List(Course)
    course = graphene.Field(Course, course_id=graphene.Int())

    def resolve_courses(self, info, **kwargs):
        return CourseModel.objects.all().order_by('id')

    def resolve_course(self, info, course_id):
        return CourseModel.objects.get(pk=course_id)

