TWITTER_AUTH = {
	'CONSUMER_TOKEN': 'get this from dev.twitter.com',
	'CONSUMER_SECRET': 'get this from dev.twitter.com',
	'ACCESS_TOKEN_KEY': 'get this from dev.twitter.com',
	'ACCESS_TOKEN_SECRET': 'get this from dev.twitter.com',
}

DM_RECIPIENTS = ['twitter_username_here', 'another_username']


import os
LOG_FILE = os.path.join(os.path.dirname(__file__), 'kerberos.log')

WATCH_LOG = '/var/log/auth.log'
MATCH_LINES = r'Accepted \S+ for \S+ from \S+'


# Try to import user overrides from settings_local.py.
try:
	from settings_local import *
except ImportError:
	pass
