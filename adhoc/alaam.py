import signal
import time

def handler(signum, stack):
    print 'Alarm: ', time.ctime()

signal.signal(signal.SIGALRM, handler)
for i in range(1000):
    signal.alarm(5)
    time.sleep(10)
    print "interrupted #%d" % i
