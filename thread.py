
import time
import thread as thd

# thread function

def printTime(thdName, delay):
  count = 0
  while count < 5:
    time.sleep(delay)
    count += 1
    print '%s %s ' % (thdName, time.ctime(time.time()))
  print 'Exiting thread', thdName

# test code

try:
  thd.start_new_thread(printTime, ('Thread 1', 2))
  thd.start_new_thread(printTime, ('Thread 2', 4))
except:
  print 'Error: unable to start threads'

# waiting for thread execution

while 1:
  pass
