kerberos
========

This little daemon monitors `/var/log/auth.log` and sends you a direct message on Twitter every time somebody logs in successfully. Intended to keep an eye on small servers which normally don't see more than a few logins a week.

You can also easily reconfigure it to watch a different log file for different messages. The basic logic is IF *log line matches a regexp* THEN *send a direct message*.


Installation
------------
  1. Clone the repo: `git clone https://github.com/ze-phyr-us/kerberos.git && cd kerberos`
  2. (Optional) Set up a Python virtual environment: `virtualenv env && source env/bin/activate`
  3. Install dependencies: `pip install -r requirements.txt`
  4. Configure (see below).
  5. `./kerberos.py` (or `./kerberos.py --foreground` to prevent daemonizing).

Kerberos will log to `kerberos.log` in the same directory where `kerberos.py` is.

You will also want to start the deamon on boot. A quick and dirty method is to add a `su username -c ...` line to `/etc/rc.local`. Use su or sudo to drop root privileges. However, the user you run this under must have read access to the log file (on Ubuntu that means being in the `adm` group: `usermod -aG adm username`).


Configuration
-------------
Change settings in `settings.py` or create `settings_local.py` and override any options you want. At the minimum, you must set two options:

  * `TWITTER_AUTH` contains OAuth credentials for the Twitter account that will be DMing you. You get the credentials by registering your app at [dev.twitter.com](https://dev.twitter.com).
  * `DM_RECIPIENTS` contains a list of Twitter usernames that should receive the DMs.

Look out for `WATCH_LOG` and `MATCH_LINES` to change which lines from what log file get reported.
