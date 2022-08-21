from graphene_django import DjangoObjectType
from .models import Student as StudentModel
from django.contrib.auth.models import User


class User(DjangoObjectType):
    class Meta:
        model = User
        exclude = ('password',)


class Student(DjangoObjectType):
    class Meta:
        model = StudentModel
