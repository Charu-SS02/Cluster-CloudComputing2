#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/front-end/")

from front-end import flaskr as application
application.secret_key = 'group26'
