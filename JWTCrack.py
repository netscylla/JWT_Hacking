#!/usr/bin/python
#(C)2018 Netscylla
#License GNU GPL v3.0

import sys,os
import Queue
import threading
import jwt
from termcolor import colored
from optparse import OptionParser

NumOfThreads=100
queue = Queue.Queue()

def help_msg():
    print """
    ======================
    JWTCrack
    (c)2018 Netscylla
    ======================
    Disclaimer: This program is free to use at your own risk!
                More details on the disclaimer and license available here: https://github.com/netscylla/JWT_Hacking
                
    Usage: JWTCrack.py [Encoded_JWT] [Wordlist] <Algorithm>"
           Endcoded_JWT = Base64 Encoded JWT String
           Wordlist     = Dictionary wordlist file used to bruteforce the JWT
           Algorithm    = (Optional) HMAC Algorithm, default=HS256
    """
    sys.exit(1)

try: 
    if (len(sys.argv) == 4):
        encoded=sys.argv[1]
        WordList=open(sys.argv[2],'r')
        algorithm=sys.argv[3]
    elif (len(sys.argv) == 3):
        encoded=sys.argv[1]
        WordList=open(sys.argv[2],'r')
        algorithm="HS256"
    else:
        raise Exception
except:
    help_msg()
    

class checkHash(threading.Thread):
    def __init__(self,queue):
        threading.Thread.__init__(self)
        self.queue=queue
    def run(self):
        options = ["HS256","HS384","HS512"]
        if algorithm not in options: "HS256"
    
        while True:
            self.secret=self.queue.get()
            try:
                jwt.decode(encoded, self.secret, algorithm)
                print colored('Success! ['+self.secret+']','green')
                os._exit(0)
                self.queue.task_done()
            except jwt.InvalidTokenError:
                print colored('Invalid Token ['+self.secret+']','red')
            except jwt.ExpiredSignatureError:
                print colored('Token Expired ['+self.secret+']','red')
                
    
def main():    

    for i in range(NumOfThreads):
        t=checkHash(queue)
        t.setDaemon(True)
        t.start()

    for word in WordList.readlines():
        queue.put(word.strip())

    queue.join()

if __name__ == '__main__':
    main()
