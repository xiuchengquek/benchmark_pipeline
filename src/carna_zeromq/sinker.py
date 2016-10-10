import zmq
import sys
import yaml
import os



config_file =  os.path.join(os.path.dirname(__file__) , 'config.yaml')


with open(config_file) as f:
    config = yaml.load(f)

sinker_reciever_ip =  config['sinker_listen']





def main(receiver_ip):
    context = zmq.Context()
    # Get reciever
    receiver = context.socket(zmq.PULL)
    receiver.bind('tcp://*:5556')
    while True:
        msg = receiver.recv_unicode()
        print(msg)

if __name__ == '__main__':
    main(sinker_reciever_ip)
