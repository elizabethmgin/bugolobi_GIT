from flask import render_template, flash, redirect
from app import app
from peewee import *
import sys

@app.route('/')
@app.route('/index/<password>')
def index(password):
    print >> sys.stderr, "within index"
    try:
        if password == 'secret':
            print >> sys.stderr, "within try"
            sellerList = Seller.select()
            smsList = SMS.select()
            numberList = Number.select()
            l = List.select()
            marketList = Market.select()
            lrList = ListRelationship.select()
            outboxList = Outbox.select()
            return render_template("index.html", title = 'TABLES', sellerList = sellerList, smsList = smsList, l = l, marketList = marketList)
            #return 'hello world'
        else:
            print >> sys.stderr, "wrong password"
    except:
        print >> sys.stderr, "within except"
        print >> sys.stderr, str(sys.exc_info()[0]) # These write the nature of the error
        print >> sys.stderr, str(sys.exc_info()[1])
        statement = 'An exception has Occured'+ str(sys.exc_type) + '[' + str(sys.exc_value) + ']'
        return statement