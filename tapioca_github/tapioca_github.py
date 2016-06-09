# -*- coding: utf-8 -*-

from tapioca import (
    TapiocaAdapter, generate_wrapper_from_adapter, JSONAdapterMixin)
from requests_oauthlib import OAuth2

from resource_mapping import RESOURCE_MAPPING


class GithubClientAdapter(JSONAdapterMixin, TapiocaAdapter):
    api_root = 'https://api.github.com/'
    resource_mapping = RESOURCE_MAPPING

    def get_request_kwargs(self, api_params):
        client_id = api_params.get('client_id')
        return {
            'auth': OAuth2(
                client_id,
                token={'access_token': api_params.get('access_token')}
            ),
        }

    def get_iterator_list(self, response_data):
        return response_data

    def get_iterator_next_request_kwargs(self,
            iterator_request_kwargs, response_data, response):
        if "Link" in response.headers:
            links = response.headers["Link"].split(", ")
            for link in links:
                (url, rel) = link.split("; ")
                url = url[1:-1]
                rel = rel[5:-1]
                if rel == 'next':
                    return {'url': url}


Github = generate_wrapper_from_adapter(GithubClientAdapter)
