#!/usr/bin/env python

import logging, sh, shelve, sys, tweepy


def sendDm(credentials, recipients, text):
	auth = tweepy.OAuthHandler(credentials.CONSUMER_TOKEN, credentials.CONSUMER_SECRET)
	auth.set_access_token(credentials.ACCESS_TOKEN_KEY, credentials.ACCESS_TOKEN_SECRET)
	api = tweepy.API(auth)
	for user in recipients:
		api.send_direct_message(user = user, text = text)


def main(argv, settings):
	if settings.LOG_FILE:
		logging.basicConfig(filename = settings.LOG_FILE, level = logging.INFO, format='[%(asctime)s][%(levelname)s] %(message)s')

	# Open (and possibly initialize) our state database.
	#state = shelve.open(settings.STATE_DB, writeback = True)
	#if not 'reportTimes' in state:
	#	state['reportTimes'] = {}
	#state.close()

	first = True
	for line in sh.tail('-f', settings.WATCH_LOG, _iter=True):
		line = line.strip()
		if not first:
			#sendDm(settings.TWITTER_AUTH, settings.DM_TO, line)
			print line
		first = False



if __name__ == '__main__':
	import settings
	sys.exit(main(sys.argv, settings) or 0)
