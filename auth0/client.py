import base64
import hashlib
import json
import datetime

from calendar import timegm

import jwt
import requests
from requests.auth import AuthBase

from auth0 import __version__

class JWTAuth(AuthBase):
    """Attaches JSON Web Token to the given Request object."""
    def __init__(self, token):
        # setup any auth-related data here
        self.token = token

    def __call__(self, r):
        # modify and return the request
        r.headers['Authorization'] = "Bearer {}".format(self.token)
        r.headers['Auth0-Client'] = "python-auth0 {}".format(__version__)
        return r

class Client(object):

    def __init__(self, domain, client_id, client_secret):
        self.domain = domain
        self.client_id = client_id
        self.client_secret = base64.urlsafe_b64decode(client_secret)
        self.base_url = "https://{}".format(self.domain)
        self.api_url = "{}/api".format(self.base_url)

    def auth(self, scopes, lifetime=36000):
        now = datetime.datetime.now()

        payload = {
            "iat": timegm(now.utctimetuple()),
            "scopes": scopes
        }
        jti = hashlib.md5(json.dumps(payload)).hexdigest()
        payload["jti"] = jti
        payload["aud"] = self.client_id

        token = jwt.encode(payload, self.client_secret, algorithm='HS256')

        return JWTAuth(token)

    def get_rule(self, rule_name):
        pass

    def get_rules(self):
        scope = {
            "rules": {
                "actions": ["read"]
            }
        }
        response = requests.get("{}/v2/rules".format(self.api_url), auth=self.auth(scope))
        return response.json()

    def get_rule(self, _id, fields=None, include_fields=True):
        scope = {
            "rules": {
                "actions": ["read"]
            }
        }

        if fields:
            params = {
                "fields": fields,
                "include_fields": include_fields
            }

        response = requests.get("{}/v2/rules/{}".format(self.api_url, _id), params=params, auth=self.auth(scope))
        return response.json()


    def create_rule(self, body):
        scope = {
            "rules": {
                "actions": ["create"]
            }
        }

        response = requests.post("{}/v2/rules".format(self.api_url), body=body, auth=self.auth(scope))
        return response.json()

    def delete_rule(self, _id):
        scope = {
            "rules": {
                "actions": ["delete"]
            }
        }

        response = requests.delete("{}/v2/rules/{}".format(self.api_url, _id), auth=self.auth(scope))
        return response.json()

    def update_rule(self, _id, body):
        scope = {
            "rules": {
                "actions": ["update"]
            }
        }
        response = requests.patch("{}/v2/rules/{}".format(self.api_url, _id), body=body, auth=self.auth(scope))
        return response.json()

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

    def get_connections(self, strategy=None, fields=None, include_fields=True):
        scope = {
            "connections": {
                "actions": ["read"]
            }
        }

        params = {
            "strategy": strategy
        }
        if fields:
            params = params.extend({
                "fields": fields,
                "include_fields": include_fields
            })

        response = requests.get("{}/v2/connections".format(self.api_url), params=params, auth=self.auth(scope))
        return response.json()

    def get_connection(self, _id, fields=None, include_fields=True):
        scope = {
            "connections": {
                "actions": ["read"]
            }
        }

        if fields:
            params = {
                "fields": fields,
                "include_fields": include_fields
            }

        response = requests.get("{}/v2/connections/{}".format(self.api_url, _id), params=params, auth=self.auth(scope))
        return response.json()


    def create_connection(self, body):
        scope = {
            "connections": {
                "actions": ["create"]
            }
        }

        response = requests.post("{}/v2/connections".format(self.api_url), body=body, auth=self.auth(scope))
        return response.json()

    def delete_connection(self, _id):
        scope = {
            "connections": {
                "actions": ["delete"]
            }
        }

        response = requests.delete("{}/v2/connections/{}".format(self.api_url, _id), auth=self.auth(scope))
        return response.json()

    def update_connection(self, _id, body):
        scope = {
            "connections": {
                "actions": ["update"]
            }
        }
        response = requests.patch("{}/v2/connections/{}".format(self.api_url, _id), body=body, auth=self.auth(scope))
        return response.json()

    def delete_tenant(self, name):
        pass

    def create_client(self, body):
        scope = {
            "clients": {
                "actions": ["create"]
            }
        }
        response = requests.post("{}/v2/clients".format(self.api_url), body=body, auth=self.auth(scope))
        return response.json()

    def update_client(self, _id, body):
        scope = {
            "clients": {
                "actions": ["update"]
            },
            "client_keys": {
                "actions": ["update"]
            }
        }
        response = requests.patch("{}/v2/clients/{}".format(self.api_url, _id), body=body, auth=self.auth(scope))
        return response.json()

    def delete_client(self, _id):
        scope = {
            "clients": {
                "actions": ["delete"]
            }
        }

        response = requests.delete("{}/v2/clients/{}".format(self.api_url, _id), auth=self.auth(scope))
        return response.json()

    def get_client(self, _id, fields=None, include_fields=True):
        scope = {
            "clients": {
                "actions": ["read"]
            },
            "client_keys": {
                "actions": ["read"]
            }
        }

        if fields:
            params = {
                "fields": fields,
                "include_fields": include_fields
            }

        response = requests.get("{}/v2/clients/{}".format(self.api_url, _id), params=params, auth=self.auth(scope))
        return response.json()

    def get_clients(self, fields=None, include_fields=True):
        scope = {
            "clients": {
                "actions": ["read"]
            },
            "client_keys": {
                "actions": ["read"]
            }
        }

        params = {}
        if fields:
            params = {
                "fields": fields,
                "include_fields": include_fields
            }

        response = requests.get("{}/v2/clients".format(self.api_url), params=params, auth=self.auth(scope))
        return response.json()

    def get_logs(self, options):
        pass
