import graphene
from .types import User, Student
from portal.apps.courses.types import ObjectField
from portal.apps.courses.models import Course as CourseModel
from .models import Student as StudentModel
from django.contrib.auth.models import User as UserModel
from django.db import IntegrityError


class Query(graphene.ObjectType):
    users = graphene.List(User)
    user = graphene.Field(User, user_id=graphene.Int())
    students = graphene.List(Student)
    student = graphene.Field(Student, student_id=graphene.Int())
    student_by_email = graphene.Field(Student, email=graphene.String(required=True))

    def resolve_users(self, info, **kwargs):
        return UserModel.objects.all().order_by('id')

    def resolve_user(self, info, user_id):
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None

    def resolve_students(self, info, **kwargs):
        return StudentModel.objects.all().order_by('id')

    def resolve_student(self, info, student_id):
        try:
            return StudentModel.objects.get(id=student_id)
        except StudentModel.DoesNotExist:
            return None

    def resolve_student_by_email(self, info, email):
        try:
            return StudentModel.objects.get(email=email)
        except StudentModel.DoesNotExist:
            return None


class CreateStudentMutation(graphene.Mutation):
    student = graphene.Field(Student)
    message = ObjectField()
    status = graphene.Int()

    class Arguments:
        username = graphene.String(required=True)
        email = graphene.String(required=True)
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        gender = graphene.String(required=True)
        password = graphene.String(required=True)
        course_id = graphene.Int(required=True)
        is_active = graphene.String()

    @classmethod
    def mutate(cls, root, info, username, email, first_name, last_name, gender, password, course_id, is_active):
        try:
            student = StudentModel(
                username=username, email=email, first_name=first_name, last_name=last_name, gender=gender,
                is_active=is_active, password=password)
            course = CourseModel.objects.get(id=course_id)
            student.course = course
            student.save()
            msg = 'success'
        except IntegrityError as e:
            student = None
            msg = 'username or email already in use'
        return cls(student=student, message=msg, status=200)


class Mutation(graphene.ObjectType):
    create_student = CreateStudentMutation.Field()
