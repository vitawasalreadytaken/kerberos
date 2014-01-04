#!/usr/bin/env python

import daemon, logging, re, sh, sys, tweepy


def sendDm(credentials, recipients, text):
	auth = tweepy.OAuthHandler(credentials.CONSUMER_TOKEN, credentials.CONSUMER_SECRET)
	auth.set_access_token(credentials.ACCESS_TOKEN_KEY, credentials.ACCESS_TOKEN_SECRET)
	api = tweepy.API(auth)
	for user in recipients:
		logging.info('Sending "%s" to @%s.', text, user)
		api.send_direct_message(user = user, text = text)


def main(argv, settings):
	logging.basicConfig(filename = settings.LOG_FILE, level = logging.DEBUG, format='[%(asctime)s][%(levelname)s] %(message)s')

	first = True
	for line in sh.tail('-f', settings.WATCH_LOG, _iter=True):
		line = line.strip()
		if not first:
			match = re.search(settings.MATCH_LINES, line)
			logging.debug('Looking for "%s" in "%s" -> %r.', settings.MATCH_LINES, line, bool(match))
			if match:
				message = '{0}: {1}'.format(sh.hostname('-s').strip(), match.group(0))
				sendDm(settings.TWITTER_AUTH, settings.DM_RECIPIENTS, message)

		first = False



if __name__ == '__main__':
	import settings
	if '--foreground' not in sys.argv:
		d = daemon.DaemonContext()
		d.open()
	sys.exit(main(sys.argv, settings) or 0)
