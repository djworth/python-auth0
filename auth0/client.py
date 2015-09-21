import base64
import hashlib
import json
import time

import jwt
import requests
from requests.auth import AuthBase


class JWTAuth(AuthBase):
    """Attaches JSON Web Token to the given Request object."""
    def __init__(self, token):
        # setup any auth-related data here
        self.token = token

    def __call__(self, r):
        # modify and return the request
        r.headers['Authorization'] = "Bearer {}".format(self.token)
        return r

class Client(object):

    def __init__(self, domain, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.domain = domain
        self.base_url = "https://{}".format(self.domain)
        self.api_url = "{}/api".format(self.base_url)

    def auth(self, scopes, lifetime=36000):
        t = int(time.time())
        payload = {
            "iat": t,
            "scopes": scopes
        }
        jti = hashlib.md5(json.dumps(payload)).hexdigest()
        payload["jti"] = jti
        payload["aud"] = self.client_id

        token = jwt.encode(payload, self.client_secret, algorithm='HS256')

        print payload
        print token

        return JWTAuth(token)

    def get_rule(self, rule_name):
        pass

    def get_rules(self):
        response = requests.get("{}/v2/rules".format(self.api_url), auth=self.auth({"rules":{"actions":["read"]}}))
        return response.json()

    def update_rule(self, rule):
        pass

    def delete_rule(self, rule_name):
        pass

    def create_rule(self, rule):
        pass

    def get_connections(self):
        pass

    def get_social_connections(self):
        pass

    def get_enterprise_connections(self):
        pass

    def get_social_users(self, options):
        pass

    def get_enterprise_users(self, options):
        pass

    def get_user(self, user_id):
        pass

    def get_user_by_search(self, search_criteria):
        pass

    def create_user(self, user_data):
        pass

    def update_user_email(self, user_id, email, verify):
        pass

    def update_user_password(self, user_id, new_password, verify):
        pass

    def get_user_metadata(self, user_id):
        pass

    def update_user_metadata(self, user_id, metadata):
        pass

    def patch_user_metadata(self, user_id, metadata):
        pass

    def delete_user(self, user_id):
        pass

    def impersonate_user(self, user_id, options):
        pass

    def get_users(self, options):
        pass

    def update_template(self, strategy, options):
        pass

    def get_template(self, strategy):
        pass

    def delete_template(self, strategy):
        pass

    def get_strategies(self):
        pass

    def get_connectd(self, name):
        pass

    def create_connection(self, connection):
        pass

    def delete_connection(self, name):
        pass

    def update_connection(self, connection):
        pass

    def delete_tenant(self, name):
        pass

    def create_client(self, options):
        pass

    def update_client(self, client):
        pass

    def delete_client(self, client_id):
        pass

    def get_clients(self, client_id):
        pass

    def getClientsByUserId(self, user_id):
        pass

    def get_logs(self, options):
        pass
