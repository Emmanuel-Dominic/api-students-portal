from snapshottest import TestCase
from graphene.test import Client
from portal.apps.users.models import Student
from django.contrib.auth.models import User
from mixer.backend.django import mixer
from portal.schema import schema


class StudentSnapshotCase(TestCase):

    def setUp(self):
        self.client = Client(schema)
        self.user1 = mixer.blend(User)
        self.user2 = mixer.blend(User)
        self.student1 = mixer.blend(Student)
        self.student2 = mixer.blend(Student)

    def test_api_view_user_snapshot(self):
        COURSES_QUERY = '''
            query {
                user(userId: 1) {
                    id
                    email
                    username
                    isActive
                    isSuperuser
                    dateJoined
                }
            }
        '''
        response = self.client.execute(COURSES_QUERY, variables={"pk": 1})
        self.assertMatchSnapshot(response)

    def test_api_view_users_snapshot(self):
        USERS_QUERY = '''
            query {
                users {
                    id
                    email
                    username
                    isActive
                    isSuperuser
                    dateJoined
                }
            }
            '''
        response = self.client.execute(USERS_QUERY)
        self.assertMatchSnapshot(response)

    def test_api_view_student_snapshot(self):
        COURSES_QUERY = '''
             query {
              student(studentId:1) {
                id
                email
                username
                isActive
                course {
                  id
                  name
                  description
                }
              }
            }
        '''
        response = self.client.execute(COURSES_QUERY, variables={"pk": 1})
        self.assertMatchSnapshot(response)

    def test_api_view_students_snapshot(self):
        COURSES_QUERY = '''
            query {
                students {
                    id
                    email
                    username
                    isActive
                    course {
                        id
                        name
                        description
                    }
                }
            }
            '''
        response = self.client.execute(COURSES_QUERY)
        self.assertMatchSnapshot(response)
