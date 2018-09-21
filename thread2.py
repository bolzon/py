import time
import threading

def worker(msg):
  for i in range(5):
    print msg
    time.sleep(0.5)

t = threading.Thread(worker, ("Thread executing",))
t.start()

while 1:
  pass

