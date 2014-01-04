import os
from dicto import dicto

LOG_FILE = None #os.path.join(os.path.dirname(__file__), 'kerberos.log')
STATE_DB = os.path.join(os.path.dirname(__file__), 'state.db')

WATCH_LOG = '/var/log/auth.log'

TWITTER_AUTH = dicto({
	'CONSUMER_TOKEN': '',
	'CONSUMER_SECRET': '',
	'ACCESS_TOKEN_KEY': '',
	'ACCESS_TOKEN_SECRET': '',
})

DM_TO = ()

MIN_REPORT_INTERVAL = 7200


try:
	from settings_local import *
except ImportError:
	pass
