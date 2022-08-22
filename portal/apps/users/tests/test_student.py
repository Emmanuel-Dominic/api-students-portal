import json
from portal.apps.courses.tests.test_base import BaseUnitTestCase


class StudentUnitTestCase(BaseUnitTestCase):

    def test_student_response(self):
        STUDENT_QUERY = '''
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
        response = self.query(
            STUDENT_QUERY,
            variables={"pk": 1}
        )
        content = json.loads(response.content)
        self.assertResponseNoErrors(response)

    def test_students_response(self):
        STUDENTS_QUERY = '''
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
        response = self.query(
            STUDENTS_QUERY
        )
        content = json.loads(response.content)
        self.assertResponseNoErrors(response)
        assert len(content['data']['students']) == 2

    def test_create_student_response(self):
        CREATE_STUDENT_MUTATION = '''
            mutation createStudent($username: String!, $email: String!, $firstName: String!, $lastName: String!, 
            $gender: String!, $password: String!, $courseId: Int!, $isActive: String!){
                createStudent(username:$username, email:$email, firstName:$firstName, lastName:$lastName, 
                gender:$gender, password:$password, courseId:$courseId, isActive:$isActive) {
                    student {
                         id 
                         username
                         email
                         firstName
                         lastName
                         gender
                         password
                         isActive
                         course { 
                            id 
                            name 
                            description
                         }
                    }
                }
            }
        '''
        response = self.query(
            CREATE_STUDENT_MUTATION,
            variables={
                "username": "username", "email": "email@gmail.com", "firstName": "first", "lastName": "last",
                "gender": "female", "password": "password123", "courseId": 1, "isActive": "t"
            }
        )
        content = json.loads(response.content)
        self.assertResponseNoErrors(response)
        assert content['data']['createStudent']['student']['username'] == 'username'
        assert content['data']['createStudent']['student']['email'] == 'email@gmail.com'

    def test_update_student_response(self):
        UPDATE_STUDENT_MUTATION = '''
            mutation updateStudent($pk:ID!, $username:String, $email:String, $firstName:String, $lastName:String, 
            $courseId:Int, $gender:String, $isActive:String){
                updateStudent(pk:$pk, username:$username, email:$email, firstName:$firstName, lastName:$lastName, 
                courseId:$courseId, gender:$gender, isActive:$isActive) {
                    student {
                        id 
                        username
                        email
                        firstName
                        lastName
                        gender
                        isActive
                    }
                }
            }
        '''
        response = self.query(
            UPDATE_STUDENT_MUTATION,
            variables={
                "pk": 1, "username": "manuel", "email": "manuel@gmail.com", "firstName": "first", "lastName": "last",
                "gender": "female", "password": "password123", "courseId": 1, "isActive": "t"
                }
        )
        content = json.loads(response.content)
        self.assertResponseNoErrors(response)
        assert content['data']['updateStudent']['student']['username'] == 'manuel'
        assert content['data']['updateStudent']['student']['email'] == 'manuel@gmail.com'

    def test_delete_student_response(self):
        DELETE_STUDENT_MUTATION = '''
            mutation deleteStudent($pk:ID!){
                deleteStudent(pk:$pk) {
                    message 
                }
            }
        '''
        response = self.query(
            DELETE_STUDENT_MUTATION,
            variables={"pk": 1}
        )
        content = json.loads(response.content)
        self.assertResponseNoErrors(response)
        assert content['data']['deleteStudent']['message'] == 'success'
