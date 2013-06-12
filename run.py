#!flask/bin/python

import sys
sys.path.insert(0, '..')

from app import app
app.run(host='10.0.1.4', debug = True)

#from app import app
#app.run(debug = True)