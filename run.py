#!flask/bin/python

import sys
sys.path.insert(0, '..')

from app import app
app.run(debug = DEBUG)

#from app import app
#app.run(debug = True)