




import zmq
import subprocess
import sys

import yaml


with open('config.yaml') as f:
    config = yaml.load(f)



ventilator_ip = config['ventilator_ip']
sinker_reciever_ip =  config['worker_to_sinker_ip']




def main(reciever_ip, sinker_ip):
    context = zmq.Context()

    # Get reciever
    receiver = context.socket(zmq.PULL)
    receiver.connect(reciever_ip)

    sinker = context.socket(zmq.PUSH)
    sinker.connect(sinker_ip)

    while True:
        bash_cmd = receiver.recv_unicode()
        p = subprocess.check_call(bash_cmd, shell=True)
        if (p == 1):
            sinker.send_unicode(u'%s fails\n' % bash_cmd)
        elif ( p == 0):
            sinker.send_unicode(u"%s completed\n"  % bash_cmd)

if __name__ == '__main__' :
    main(ventilator_ip, sinker_reciever_ip)

