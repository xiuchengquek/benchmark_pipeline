import os



import zmq
import sys

import yaml





if __name__ == '__main__':


    context = zmq.Context()
    sender = context.socket(zmq.PUSH)
    sender.bind('tcp://*:5555')
   
  
    with open(sys.argv[1]) as f:
        for line in f:
            sender.send_unicode(u'%s' % line)
    









