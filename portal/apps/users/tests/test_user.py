import json
from portal.apps.courses.tests.test_base import BaseUnitTestCase


class UserUnitTestCase(BaseUnitTestCase):

    def test_user_response(self):
        user_QUERY = '''
            query user($pk: Int!){
                user(userId: $pk) {
                    id
                    email
                    username
                    isActive
                    isSuperuser
                    dateJoined
                }
            }
            '''
        response = self.query(
            user_QUERY,
            variables={"pk": 1}
        )
        content = json.loads(response.content)
        self.assertResponseNoErrors(response)

    def test_users_response(self):
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
        response = self.query(
            USERS_QUERY
        )
        content = json.loads(response.content)
        self.assertResponseNoErrors(response)
        assert len(content['data']['users']) == 2
