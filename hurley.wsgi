import sys
import site

site.addsitedir("/home/alexwlchan/.virtualenvs/hurley/local/lib/python2.7/site-packages")

# Expand Python classes path with your app's path
sys.path.insert(0, "/var/www/six-degrees-of-myke/hurley")

from hurley import app

# Put logging code (and imports) here ...

# Initialize WSGI app object
application = app
