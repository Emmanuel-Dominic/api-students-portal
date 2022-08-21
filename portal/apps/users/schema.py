import graphene
from .types import User, Student
from .models import Student as StudentModel
from django.contrib.auth.models import User as UserModel


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
