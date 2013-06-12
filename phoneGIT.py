import datetime
import android, time
import pprint
import json
import requests
import sys
import ast

emails = 'youremail@gmail.com'
payload = 'payload from config'
postURL = 'http://IPAddress:Port/sms_received/'
getURL = 'http://IPAddress:Port/sms_to_send/'

print "initiating droid"
droid = android.Android()

# pass list of messages
# return messageDict in json    
def create_Message_Dict(messages):
    messageDict = {}
    messageString = str(messages)
    messageDict["messages"] = messageString
    messageDict["auth"] = str(payload)
    print messageDict
    return messageDict

print "checking existing records"

# print str(SMS.select().count()) + " messages saved so far."

print "entering loop..."
while True:
    try:
        print >> sys.stderr, "within try"
        messages = droid.smsGetMessages(True).result
        if messages:
            print >> sys.stderr, "within if"
            droid.smsMarkMessageRead(droid.smsGetMessageIds(True).result,True) # mark those messages as read
            print str(len(messages)) +" new sms messages!"
            messageDict = create_Message_Dict(messages) # create message dict
            r = requests.post(postURL, params=messageDict) # pack url
        else:
            print 'no new messages!'
            r = requests.get(getURL)
            message = json.loads(r.text)
            print >> sys.stderr, message
            listStr = message['messages']
            messageList = ast.literal_eval(listStr)
            print >> sys.stderr, messageList
            if messageList:
                print >> sys.stderr, 'within messageList for'
                for message in messageList:
                    print message
                    number = '+' + str(message[0])
                    droid.smsSend(str(number),str(message[1]))
            else:
                print 'no outbox messages!'
    except:
        print >> sys.stderr, "within except"
        # droid.sendEmail(emails, 'An exception has Occured', str(sys.exc_type) + '[' + str(sys.exc_value) + ']')
    time.sleep(15)




