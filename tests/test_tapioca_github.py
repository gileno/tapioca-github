import unittest

import responses

from tapioca_github import Github
from tapioca_github.resource_mapping import RESOURCE_MAPPING
from tests.fixtures import SINGLE_GIST_PAYLOAD


class TestTapioca(unittest.TestCase):

    def setUp(self):
        self.wrapper = Github(access_token='access_token_token')

    def test_resource_access(self):
        with responses.RequestsMock(assert_all_requests_are_fired=True) as rsps:
            test_gist_id = 1
            rsps.add(
                responses.GET,
                'https://api.github.com/' +
                RESOURCE_MAPPING['gists_single']['resource'].format(id=test_gist_id),
                json=SINGLE_GIST_PAYLOAD, status=201)

            resource = self.wrapper.gists_single(id=test_gist_id).get()
            self.assertEqual(resource().data, SINGLE_GIST_PAYLOAD)


if __name__ == '__main__':
    unittest.main()
