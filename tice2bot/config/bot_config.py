""" Config File """

####################################
# TELEGRAM
####################################

# Change this to your telegram token
TOKEN = '5734765428:AAGcdtPd4fmyFtwcn3Zyi1kwMfJVjoCynZg'

# List of bot owners

BOT_OWNERS = [
    '@cryptalien5'  # telegram username
]

###################################
# ICECAST2
###################################

# List of your IceCast2 servers.

ICECAST2_SERVERS = [
    'cryptoafterdark.caster.fm:8000',
    'cryptoafterdark.caster.fm:8000',
]

# by default status-json.xsl will return http protocol even ssl is set to 1 in
# icecast.xml, so when we want and we want! to use SSL this flag must be set to True

SSL = True

# IceCast2 status files, depenends on IceCast2 config file.
# this web resource is public by default, so we used it to fetch
# statistics about the icecast2 server

ICECAST2_STATS_FILE = 'status-json.xsl'

# How many radio links can I serve?

SERVERS_LIMIT = 100

# icecast authentication web hooK
# this web hook is used by icecast2 url settings and specialy from listener_add
# more info @ https://icecast.org/docs/icecast-2.4.0/auth.html
# in our case the auth hook point to one of our stream server, but can be anything else.

WEBHOOK_IP = "http://shaincast.caster.fm:18372/listen.mp3?authn77d66ea62cd7ae9d770565c04a9b9fdb"
WEBHOOK_PORT = 8000

###################################
# Redis settings
###################################

REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 0
REDIS_SESSION_EXPIRE = 8 * 3600

