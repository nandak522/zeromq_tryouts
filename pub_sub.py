#publisher
import zmq
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind('tcp://127.0.0.1:8000')
for i in range(1, 10):
    print '%s Mail sent' % i
    socket.send(str(i))
    
    


#subscriber 1 ==> On iPad
import zmq
from datetime import datetime
timestamp = datetime.strftime(datetime.now(), '%H:%M:%S')
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect('tcp://127.0.0.1:8000')
socket.setsockopt(zmq.SUBSCRIBE, '')
while True:
    msg = socket.recv()
    print 'on iPad %s Mails Received at %s' % (msg, timestamp)
    


#subscriber 2 ==> On Laptop
import zmq
from datetime import datetime
timestamp = datetime.strftime(datetime.now(), '%H:%M:%S')
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect('tcp://127.0.0.1:8000')
socket.setsockopt(zmq.SUBSCRIBE, '')
while True:
    msg = socket.recv()
    print 'on Laptop %s Mails Received at %s' % (msg, timestamp)
    

