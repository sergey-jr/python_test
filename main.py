import requests


def main(login='test', password=12345, username='ivanov'):
    base_url = 'http://testapi.ru'

    response = requests.get(base_url, auth=(login, password))
    test_var = {'login': 'BAD', 'get_user': 'BAD', 'update': 'BAD'}
    if response.status_code == 200:
        data = response.json()
        test_var['login'] = data['status']
        if data['status'] == 'OK':
            token = data['token']
            response = requests.get(base_url + '/get-user/{}'.format(username),
                                    params={'token': token})
            if response.status_code == 200:
                data = response.json()
                test_var['get_user'] = data['status']
                if data['status'] == 'OK':
                    user_id = data['user_id']
                    post_data = {
                        'active': '1',
                        'blocked': True,
                        'name': 'Petr Petrovich',
                        'permissions': [
                            {
                                'id': 1,
                                'permission': 'comment'
                            },
                        ]
                    }
                    response = requests.post(base_url + '/user/{}/update'.format(user_id),
                                             params={'token': token},
                                             json=post_data)
                    data = response.json()
                    test_var['update'] = data['status']
    return test_var
