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
    'events_public': {
        'resource': 'events',
        'doc': 'https://developer.github.com/v3/activity/events/#list-public-events',
    },
    'events_repository': {
        'resource': 'repos/{owner}/{repo}/events',
        'doc': 'https://developer.github.com/v3/activity/events/#list-repository-events'
    },
    'events_issues': {
        'resource': 'repos/{owner}/{repo}/issues/events',
        'doc': 'https://developer.github.com/v3/activity/events/#list-issue-events-for-a-repository'
    },
    'events_network': {
        'resource': 'networks/{owner}/{repo}/events',
        'doc': 'https://developer.github.com/v3/activity/events/#list-public-events-for-a-network-of-repositories'
    },
    'events_organization': {
        'resource': 'orgs/{org}/events',
        'doc': 'https://developer.github.com/v3/activity/events/#list-public-events-for-an-organization'
    },
    'events_user_received': {
        'resource': 'users/{username}/received_events',
        'doc': 'https://developer.github.com/v3/activity/events/#list-events-that-a-user-has-received'
    },
    'events_user_received_public': {
        'resource': 'users/{username}/received_events/public',
        'doc': 'https://developer.github.com/v3/activity/events/#list-public-events-that-a-user-has-received'
    },
    'events_user': {
        'resource': 'users/{username}/events',
        'doc': 'https://developer.github.com/v3/activity/events/#list-events-performed-by-a-user'
    },
    'events_user_public': {
        'resource': 'users/{username}/events/public',
        'doc': 'https://developer.github.com/v3/activity/events/#list-public-events-performed-by-a-user'
    },
    'events_user_organization': {
        'resource': 'users/{username}/events/orgs/{org}',
        'doc': 'https://developer.github.com/v3/activity/events/#list-events-for-an-organization'
    },
}
