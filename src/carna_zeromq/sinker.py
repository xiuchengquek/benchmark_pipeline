import zmq
import sys
import yaml


with open('config.yaml') as f:
    config = yaml.load(f)

sinker_reciever_ip =  config['sinker_listen']





def main(receiver_ip):
    context = zmq.Context()
    # Get reciever
    receiver = context.socket(zmq.PULL)
    receiver.bind(receiver_ip)
    while True:
        msg = receiver.recv_unicode()
        print(msg)

if __name__ == '__main__':
    main(sinker_reciever_ip)
