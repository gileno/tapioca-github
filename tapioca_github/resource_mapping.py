# coding=utf-8

RESOURCE_MAPPING = {
    'gists_user': {
        'resource': 'users/{username}/gists',
        'doc': 'https://developer.github.com/v3/gists/#list-gists'
    },
    'gists': {
        'resource': 'gists',
        'doc': 'https://developer.github.com/v3/gists/#list-gists'
    },
    'gists_public': {
        'resource': 'gists/public',
        'doc': 'https://developer.github.com/v3/gists/#list-gists'
    },
    'gists_starred': {
        'resource': 'gists/starred',
        'doc': 'https://developer.github.com/v3/gists/#list-gists'
    },
    'gists_single': {
        'resource': 'gists/{id}',
        'doc': 'https://developer.github.com/v3/gists/#get-a-single-gist'
    },
    'gists_single_revision': {
        'resource': 'gists/{id}/{sha}',
        'doc': 'https://developer.github.com/v3/gists/' \
               '#get-a-specific-revision-of-a-gist'
    },
    'gists_single_commits': {
        'resource': 'gists/{id}/commits',
        'doc': 'https://developer.github.com/v3/gists/#list-gist-commits'
    },
    'gists_star': {
        'resource': 'gists/{id}/star',
        'doc': 'https://developer.github.com/v3/gists/#star-a-gist'
    },
    'gists_forks': {
        'resource': 'gists/{id}/forks',
        'doc': 'https://developer.github.com/v3/gists/#fork-a-gist'
    },
}
