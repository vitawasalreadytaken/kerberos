import os
from dicto import dicto

LOG_FILE = os.path.join(os.path.dirname(__file__), 'kerberos.log')

WATCH_LOG = '/var/log/auth.log'
MATCH_LINES = r'Accepted \S+ for \S+ from \S+'

TWITTER_AUTH = dicto({
	'CONSUMER_TOKEN': '',
	'CONSUMER_SECRET': '',
	'ACCESS_TOKEN_KEY': '',
	'ACCESS_TOKEN_SECRET': '',
})

DM_RECIPIENTS = ()


try:
	from settings_local import *
except ImportError:
	pass
