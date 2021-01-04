import requests


class TestApi:
    def __init__(self, base_url):
        self.base_url = base_url
        self.token = None

    def auth(self, login, password):
        response = requests.get(self.base_url + '/auth',
                                auth=(login, password))
        if response.status_code != 200:
            raise Exception('Error happened while getting auth url')
        data = response.json()
        if data['status'] != 'OK':
            raise Exception('Error happened while login')
        self.token = data['token']
        return data

    def get_user(self, username):
        response = requests.get(self.base_url + '/get-user/{}'.format(username),
                                params={'token': self.token})
        if response.status_code != 200:
            raise Exception('Error happened while getting user-get url')
        data = response.json()
        if data['status'] != 'OK':
            raise Exception('Error happened while getting user data, status={}'.format(data['status']))
        return data

    def update_user(self, user_id, post_data):
        response = requests.post(self.base_url + '/user/{}/update'.format(user_id),
                                 params={'token': self.token},
                                 json=post_data)
        if response.status_code != 200:
            raise Exception('Error happened while getting user-update url')
        data = response.json()
        if data['status'] != 'OK':
            raise Exception('Error happened while updating user')
        return data
