# pytest
import json
import pytest
from graphene_django.utils.testing import graphql_query


@pytest.fixture
def client_query(client):
    def func(*args, **kwargs):
        return graphql_query(*args, **kwargs, client=client)
    return func


@pytest.fixture
def new_course(client):
    NEW_COURSE_MUTATION = '''
        mutation {
            createCourse(name:"course name", description:"course description") {
                course {
                  id 
                  name
                  description
                }
            }
        }
        '''
    return NEW_COURSE_MUTATION


@pytest.fixture
def new_student(client):
    NEW_student_MUTATION = '''mutation { createStudent(username:"username", email:"email@gmail.com", 
    firstName:"fname", lastName:"lname", gender:"female", password:"pass12345", courseId:1, isActive: "t") { student { 
    id username email firstName lastName gender password isActive course { id name description } } } }
    '''
    return NEW_student_MUTATION


@pytest.fixture
def student_one(client):
    student_QUERY = '''
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
    return student_QUERY


@pytest.fixture
def students(client):
    studentS_QUERY = '''
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
    return studentS_QUERY


@pytest.fixture
def update_student(client):
    UPDATE_student_MUTATION = '''mutation { updateStudent(pk:1, username:"username", email:"email@gmail.com", 
    firstName: "first", lastName: "last", courseId: 1, gender: "male", isActive: "t") { student { id username email 
    firstName lastName gender isActive } } } 
    '''
    return UPDATE_student_MUTATION


@pytest.fixture
def delete_student(client):
    DELETE_student_MUTATION = '''
        mutation {
            deleteStudent(pk:1) {
                message 
            }
        }
        '''
    return DELETE_student_MUTATION


@pytest.mark.django_db
def test_create_student_query(client_query, new_course, new_student):
    resp = client_query(new_course)
    new_content = json.loads(resp.content)
    response = client_query(new_student)
    content = json.loads(response.content)
    assert 'errors' not in content
    assert 'errors' not in new_content


@pytest.mark.django_db
def test_student_query(client_query, new_course, new_student, student_one):
    course_resp = client_query(new_course)
    course_content = json.loads(course_resp.content)
    resp = client_query(new_student)
    response = client_query(student_one)
    new_content = json.loads(resp.content)
    content = json.loads(response.content)
    assert 'errors' not in content
    assert 'errors' not in new_content
    assert 'errors' not in course_content


@pytest.mark.django_db
def test_students_query(client_query, students):
    response = client_query(students)
    content = json.loads(response.content)
    assert 'errors' not in content


@pytest.mark.django_db
def test_update_student_query(client_query, new_course, new_student, update_student):
    course_resp = client_query(new_course)
    course_content = json.loads(course_resp.content)
    resp = client_query(new_student)
    new_content = json.loads(resp.content)
    response = client_query(update_student)
    content = json.loads(response.content)
    assert 'errors' not in content
    assert 'errors' not in new_content
    assert 'errors' not in course_content


@pytest.mark.django_db
def test_delete_student_query(client_query, new_course, new_student, delete_student):
    course_resp = client_query(new_course)
    course_content = json.loads(course_resp.content)
    resp = client_query(new_student)
    new_content = json.loads(resp.content)
    response = client_query(delete_student)
    content = json.loads(response.content)
    assert 'errors' not in content
    assert 'errors' not in new_content
    assert 'errors' not in course_content
