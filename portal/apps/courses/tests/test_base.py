from graphene_django.utils.testing import GraphQLTestCase
from portal.apps.courses.models import Course
from portal.apps.users.models import Student
from django.contrib.auth.models import User
from mixer.backend.django import mixer
from portal.schema import schema


class BaseUnitTestCase(GraphQLTestCase):
    GRAPHQL_SCHEMA = schema

    def setUp(self):
        super().setUp()
        self.user1 = mixer.blend(User)
        self.user2 = mixer.blend(User)
        self.course1 = mixer.blend(Course)
        self.course2 = mixer.blend(Course)
        self.student1 = mixer.blend(Student)
        self.student2 = mixer.blend(Student)
