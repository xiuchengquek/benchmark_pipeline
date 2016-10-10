




import zmq
import subprocess
import sys

import yaml

import os

config_file =  os.path.join(os.path.dirname(__file__) , 'config.yaml')


with open(config_file) as f:
    config = yaml.load(f)


ventilator_ip = config['ventilator_ip']
sinker_reciever_ip =  config['worker_to_sinker_ip']




def main(reciever_ip, sinker_ip):
    context = zmq.Context()

    # Get reciever
    receiver = context.socket(zmq.PULL)
    receiver.connect('tcp://192.168.11.203:5555')

    sinker = context.socket(zmq.PUSH)
    sinker.connect('tcp://192.168.11.203:5556')

    while True:
        bash_cmd = receiver.recv_unicode()
        p = subprocess.check_call(bash_cmd, shell=True)
        if (p == 1):
            sinker.send_unicode(u'%s\tfails' % bash_cmd)
        elif ( p == 0):
            sinker.send_unicode(u"%s\tcompleted"  % bash_cmd)

if __name__ == '__main__' :
    main(ventilator_ip, sinker_reciever_ip)

