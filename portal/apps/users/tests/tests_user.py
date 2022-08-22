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
def users(client):
    userS_QUERY = '''
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
    return userS_QUERY


@pytest.mark.django_db
def test_users_query(client_query, users):
    response = client_query(users)
    content = json.loads(response.content)
    assert 'errors' not in content
