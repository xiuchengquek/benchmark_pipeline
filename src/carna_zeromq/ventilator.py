



import zmq
import sys

import yaml



config_file =  os.path.join(os.path.dirname(__file__) , 'config.yaml')


with open(config_file) as f:
    config = yaml.load(f)


worker_reciever_ip = config['worker_reciever_ip']
sinker_reciever_ip =  config['sinker_reciever_ip']

if __name__ == '__main__':


    context = zmq.Context()
    sender = context.socket(zmq.PUSH)
    sender.bind(worker_reciever_ip)
    sink = context.socket(zmq.PUSH)
    sink = sink.connect(sinker_reciever_ip)
    with open(sys.argv[1]) as f:
        for line in f:
            sender.send_unicode(u'%s' % line)
            sink.send_unicode(u"%s" % line)









