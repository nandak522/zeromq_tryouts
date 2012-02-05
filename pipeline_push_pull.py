#pusher
import zmq
context = zmq.Context()
sender = context.socket(zmq.PUSH)
sender.bind('tcp://*:8000')
for i in range(1,11):
    print 'Pushing %s' % i
    sender.send(str(i))
    


#worker 1
import zmq
context = zmq.Context()
listener = context.socket(zmq.PULL)
listener.connect('tcp://*:8000')
sink_sender = context.socket(zmq.PUSH)
sink_sender.connect('tcp://*:9000')
while True:
    received = listener.recv()
    print 'Pulled/Receiver 1 %s' % received
    sink_sender.send(str(received*2))



#worker 2
import zmq
context = zmq.Context()
listener = context.socket(zmq.PULL)
listener.connect('tcp://*:8000')
sink_sender = context.socket(zmq.PUSH)
sink_sender.connect('tcp://*:9000')
while True:
    received = listener.recv()
    print 'Pulled/Receiver 2 %s' % received
    sink_sender.send(str(received*3))
    


#sink
import zmq
context = zmq.Context()
sink = context.socket(zmq.PULL)
sink.bind('tcp://*:9000')
collector = []
for i in range(1,11):
    received = sink.recv()
    collector.append(received)
print 'Collected values:%s' % ",".join(collector)
