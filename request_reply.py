#client:
import zmq
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect('tcp://127.0.0.1:8000')
socket.connect('tcp://127.0.0.1:9000')
for i in range(10):
    print 'Client Sending ==> %s' % i
    socket.send(str(i))
    print 'Client Received ==> %s' % socket.recv()
    
    




#server:
import zmq
context = zmq.Context()
socket = context.socket(zmq.REP)
port = '9000'
socket.bind('tcp://127.0.0.1:%s' % port)
while True:
    msg = socket.recv()
    print 'Server @ %s Received ==> %s' % (port, msg)
    socket.send('Server @ %s Echoing back(sending) ==> %s' % (port, msg))
    
    
