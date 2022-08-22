import json
from .test_base import BaseUnitTestCase


class CourseUnitTestCase(BaseUnitTestCase):

    def test_course_response(self):
        COURSE_QUERY = '''
            query course($pk: Int!){
                course(courseId: $pk) {
                    id
                    name
                    description
                }
            }
            '''
        response = self.query(
            COURSE_QUERY,
            variables={"pk": 1}
        )
        content = json.loads(response.content)
        self.assertResponseNoErrors(response)

    def test_courses_response(self):
        COURSES_QUERY = '''
            query {
                courses {
                    id
                    name
                    description
                }
            }
            '''
        response = self.query(
            COURSES_QUERY
        )
        content = json.loads(response.content)
        self.assertResponseNoErrors(response)
        assert len(content['data']['courses']) == 4

    def test_create_course_response(self):
        CREATE_COURSE_MUTATION = '''
            mutation createCourse($name: String!, $description: String!){
                createCourse(name: $name, description: $description) {
                    course {
                        id
                        name
                        description
                    }
                }
            }
        '''
        description = '''The water resources engineering curriculum is designed to prepare interested students for 
        future careers in water supply, waste water, floodplain, storm water. '''
        response = self.query(
            CREATE_COURSE_MUTATION,
            variables={
                "name": "Bachelor of Science in Water Resources Engineering", "description": description}
        )
        content = json.loads(response.content)
        self.assertResponseNoErrors(response)
        assert content['data']['createCourse']['course']['name'] == 'Bachelor of Science in Water Resources Engineering'

    def test_update_course_response(self):
        UPDATE_COURSE_MUTATION = '''
            mutation updateCourse($pk: ID!, $name: String, $description: String){
                updateCourse(pk: $pk, name: $name, description: $description) {
                    course {
                        id
                        name
                        description
                    }
                }
            }
        '''
        description = '''Computer Engineering prepares the graduate for developing and using technologies, as well as 
        being able to design, produce, and manage data elaboration systems in a wide range of applications. '''
        response = self.query(
            UPDATE_COURSE_MUTATION,
            variables={
                "pk": 1, "name": "Bachelor of Computer Engineering", "description": description}
        )
        content = json.loads(response.content)
        self.assertResponseNoErrors(response)
        assert content['data']['updateCourse']['course']['name'] == 'Bachelor of Computer Engineering'

    def test_delete_course_response(self):
        DELETE_COURSE_MUTATION = '''
            mutation deleteCourse($pk: ID!){
                deleteCourse(pk: $pk) {
                    message
                }
            }
        '''
        response = self.query(
            DELETE_COURSE_MUTATION,
            variables={"pk": 1}
        )
        content = json.loads(response.content)
        self.assertResponseNoErrors(response)
        assert content['data']['deleteCourse']['message'] == 'success'
