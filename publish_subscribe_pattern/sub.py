import zmq

# ZeroMQ Context
context = zmq.Context()

# Define the socket using the "Context"
sock = context.socket(zmq.SUB)

# Define subscription and messages with prefix to accept.
sock.setsockopt(zmq.SUBSCRIBE,"1")
sock.setsockopt(zmq.SUBSCRIBE,"2")
sock.connect("tcp://127.0.0.1:5680")

while True:
        message= sock.recv()
        print message
