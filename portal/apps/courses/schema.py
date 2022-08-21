import graphene
from .types import Course, ObjectField
from .models import Course as CourseModel
from django.db import IntegrityError


class Query(graphene.ObjectType):
    courses = graphene.List(Course)
    course = graphene.Field(Course, course_id=graphene.Int())

    def resolve_courses(self, info, **kwargs):
        return CourseModel.objects.all().order_by('id')

    def resolve_course(self, info, course_id):
        return CourseModel.objects.get(pk=course_id)


class CreateCourseMutation(graphene.Mutation):
    course = graphene.Field(Course)
    message = ObjectField()
    status = graphene.Int()

    class Arguments:
        name = graphene.String(required=True)
        description = graphene.String(required=True)

    @classmethod
    def mutate(cls, root, info, name, description):
        try:
            course = CourseModel(name=name, description=description)
            course.save()
            msg = 'success'
        except IntegrityError:
            course = None
            msg = 'name already in use'
        return cls(course=course, message=msg, status=200)


class EditCourseMutation(graphene.Mutation):
    course = graphene.Field(Course)
    message = ObjectField()
    status = graphene.Int()

    class Arguments:
        # The input arguments for this mutation
        pk = graphene.ID(required=True)
        name = graphene.String()
        description = graphene.String()

    def mutate(self, info, pk, name, description):
        course = None
        try:
            course = CourseModel.objects.get(pk=pk)
            course.name = name
            course.description = description
            course.save()
            # Notice we return an instance of this mutation
            msg = 'success'
        except CourseModel.DoesNotExist:
            msg = 'Course not found'
        except IntegrityError:
            msg = 'Course name already in use'
        return EditCourseMutation(course=course, message=msg, status=200)


class DeleteCourseMutation(graphene.Mutation):
    message = ObjectField()
    status = graphene.Int()

    class Arguments:
        pk = graphene.ID(required=True)

    @classmethod
    def mutate(cls, root, info, pk, **kwargs):
        try:
            c = CourseModel.objects.get(pk=pk)
            c.delete()
            msg = 'success'
        except CourseModel.DoesNotExist:
            c = None
            msg = 'Course not found'
        return cls(message=msg, status=200)


class Mutation(graphene.ObjectType):
    create_course = CreateCourseMutation.Field()
    update_course = EditCourseMutation.Field()
    delete_course = DeleteCourseMutation.Field()
