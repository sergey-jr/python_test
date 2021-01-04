import unittest
from main import TestApi


class MyTestCase(unittest.TestCase):
    base_url = 'http://testapi.ru'
    login, password = ('test', 12345)

    def test_all(self):
        self.test_auth()
        self.test_get_user()
        self.test_update_user()

    def test_auth(self):
        test_object = TestApi(self.base_url)
        data = test_object.auth(self.login, self.password)
        self.assertEqual(data,
                         {
                             'status': 'OK',
                             'token': 'dsfd79843r32d1d3dx23d32d'
                         }
                         )

    def test_get_user(self):
        test_object = TestApi(self.base_url)
        test_object.auth(login='test', password=12345)
        data = test_object.get_user('ivanov')
        self.assertEqual(data,
                         {
                             'status': 'OK',
                             'active': '1',
                             'blocked': False,
                             'created_at': 1587457590,
                             'id': 23,
                             'name': 'Ivanov Ivan',
                             'permissions': [
                                 {
                                     'id': 1,
                                     'permission': 'comment'
                                 },
                                 {
                                     'id': 2,
                                     'permission': 'upload photo'
                                 },
                                 {
                                     'id': 3,
                                     'permission': 'add event'
                                 }
                             ]
                         }
                         )

    def test_update_user(self):
        test_object = TestApi(self.base_url)
        test_object.auth(login='test', password=12345)
        data = test_object.update_user(23,
                                       post_data={
                                           'active': '1',
                                           'blocked': True,
                                           'name': 'Petr Petrovich',
                                           'permissions': [
                                               {
                                                   'id': 1,
                                                   'permission': 'comment'
                                               },
                                           ]
                                       })
        self.assertEqual(data,
                         {
                             'status': 'OK',
                         }
                         )


if __name__ == '__main__':
    unittest.main()
