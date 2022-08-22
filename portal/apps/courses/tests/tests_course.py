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
def course_one(client):
    COURSE_QUERY = '''
        query {
            course(courseId: 1) {
                id
                name
                description
            }
        }
        '''
    return COURSE_QUERY


@pytest.fixture
def courses(client):
    COURSES_QUERY = '''
        query {
            courses {
                id
                name
                description
            }
        }
        '''
    return COURSES_QUERY


@pytest.fixture
def update_course(client):
    UPDATE_COURSE_MUTATION = '''
        mutation {
            updateCourse(pk:1, name:"update course name", description:"update course description") {
                course {
                    id 
                    name
                    description
                }
            }
        }
        '''
    return UPDATE_COURSE_MUTATION


@pytest.fixture
def delete_course(client):
    DELETE_COURSE_MUTATION = '''
        mutation {
            deleteCourse(pk:1) {
                message 
            }
        }
        '''
    return DELETE_COURSE_MUTATION


@pytest.mark.django_db
def test_create_course_query(client_query, new_course):
    response = client_query(new_course)
    content = json.loads(response.content)
    assert 'errors' not in content


@pytest.mark.django_db
def test_course_query(client_query, new_course, course_one):
    resp = client_query(new_course)
    response = client_query(course_one)
    new_content = json.loads(resp.content)
    content = json.loads(response.content)
    assert 'errors' not in content
    assert 'errors' not in new_content


@pytest.mark.django_db
def test_courses_query(client_query, courses):
    response = client_query(courses)
    content = json.loads(response.content)
    assert 'errors' not in content


@pytest.mark.django_db
def test_update_course_query(client_query, new_course, update_course):
    resp = client_query(new_course)
    new_content = json.loads(resp.content)
    response = client_query(update_course)
    content = json.loads(response.content)
    assert 'errors' not in content
    assert 'errors' not in new_content


@pytest.mark.django_db
def test_delete_course_query(client_query, new_course, delete_course):
    resp = client_query(new_course)
    new_content = json.loads(resp.content)
    response = client_query(delete_course)
    content = json.loads(response.content)
    assert 'errors' not in content
    assert 'errors' not in new_content
