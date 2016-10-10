



import zmq
import sys





worker_reciever_ip = 'tcp:://*:5555'
sinker_reciever_ip =  'tcp://localhost:5556'

if __name__ == '__main__':
    context = zmq.Context()
    sender = context.socket(zmq.PUSH)
    sender.bind(worker_reciever_ip)
    sink = context.socket(zmq.PUSH)
    sink = sink.connect(sinker_reciever_ip)
    with open(sys.argv[1]) as f:
        for line in f:
            sender.send_unicode(u'%s' % line)









