from snapshottest import TestCase
from graphene.test import Client
from portal.apps.courses.models import Course
from mixer.backend.django import mixer
from portal.schema import schema


class CourseSnapshotCase(TestCase):

    def setUp(self):
        self.client = Client(schema)
        self.course1 = mixer.blend(Course)
        self.course2 = mixer.blend(Course)

    def test_api_view_course_snapshot(self):
        COURSES_QUERY = '''
           query course($pk: Int!){
               course(courseId: $pk) {
                   id
                   name
                   description
               }
           }
        '''
        response = self.client.execute(COURSES_QUERY, variables={"pk": 1})
        self.assertMatchSnapshot(response)

    def test_api_view_courses_snapshot(self):
        COURSES_QUERY = '''
            query {
                courses {
                    id
                    name
                    description
                }
            }
            '''
        response = self.client.execute(COURSES_QUERY)
        self.assertMatchSnapshot(response)
