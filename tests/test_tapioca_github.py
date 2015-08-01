import unittest

from tapioca_github import Github


class TestTapioca(unittest.TestCase):

    def setUp(self):
        self.wrapper = Github(access_token='access_token')

    def test_resource_access(self):
        resource = self.wrapper.gists_public()

        self.assertEqual(resource.data(), 'https://api.github.com/gists/public')


if __name__ == '__main__':
    unittest.main()
