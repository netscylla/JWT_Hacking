#!/usr/bin/python
#(C)2018 Netscylla
#License GNU GPL v3.0

import sys,os
import Queue
import threading
import jwt
from termcolor import colored

NumOfThreads=100
queue = Queue.Queue()

try:
    encoded=sys.argv[1]
    WordList=open(sys.argv[2],'r')
except:
    print "Usage: %s encoded wordlist" % sys.argv[0]
    sys.exit(1)

class checkHash(threading.Thread):
    def __init__(self,queue):
        threading.Thread.__init__(self)
        self.queue=queue
    def run(self):
        while True:
            self.secret=self.queue.get()
            try:
                jwt.decode(encoded, self.secret, algorithms=['HS256'])
                print colored('Success! ['+self.secret+']','green')
                os._exit(0)
                self.queue.task_done()
            except jwt.InvalidTokenError:
                print colored('Invalid Token ['+self.secret+']','red')
            except jwt.ExpiredSignatureError:
                print colored('Token Expired ['+self.secret+']','red')

for i in range(NumOfThreads):
    t=checkHash(queue)
    t.setDaemon(True)
    t.start()

for word in WordList.readlines():
    queue.put(word.strip())

queue.join()
