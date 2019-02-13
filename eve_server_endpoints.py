class RestServer(object):

    def __init__(self, address):
        self.cookies = None
        self.base_url = '/'.join(['http:/', address, 'api'])
    
    def _send_request(self, method, path, data=None):
        response = None
        url = self.base_url + path
        try:
            response = requests.request(method, url,  json=data, cookies=self.cookies)
        except requests.exceptions.RequestException as e:
            print('*** Error calling %s: %s', url, e.message)
        return response

    def get_object(self, api_call, data=None):
        return self._send_request('GET', api_call, data)

    def add_object(self, api_call, data=None):
        return self._send_request('POST', api_call, data)

    def update_object(self, api_call, data=None):
        return self._send_request('PUT', api_call, data)

    def del_object(self, api_call, data=None):
        return self._send_request('DELETE', api_call, data)

    def set_cookies(self, cookie):
        self.cookies = cookie

REST_SCHEMA = {
    'login': '/auth/login',
    'logout': '/auth/logout',
    'status': '/status',
    'list_templates': '/list/templates/'
}

class EveServer(RestServer):

    def __init__(self, address):
        super(EveServer, self).__init__(address)

    def login(self, user, pwd):
        api_call = REST_SCHEMA['login']
        payload = {
            "username": user,
            "password": pwd
        }
        resp = self.add_object(api_call, data=payload)
        self.set_cookies(resp.cookies)
        return resp

    def logout(self):
        api_call = REST_SCHEMA['logout']
        resp = self.get_object(api_call)
        return resp

    def get_status(self):
        api_call = REST_SCHEMA['status']
        resp = self.get_object(api_call)
        return resp

    def get_templates(self):
        api_call = REST_SCHEMA['list_templates']
        resp = self.get_object(api_call)
        return resp