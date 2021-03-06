#!/usr/bin/python

import threading
import time
import os

exitFlag = 0

class myThread (threading.Thread):

   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name

   def run(self):
      print("Starting " + self.name)
      do_something(2)
      print("Exiting " + self.name)

def do_something(input): 
  time.sleep(input)
  print(input, os.getpid())

# Create new threads
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# Start new Threads
thread1.start()
thread2.start()

print("Exiting Main Thread")