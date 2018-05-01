from multiprocessing import Pool 
from timer import Timer
import time
import os
from subprocess import call

def do_something(input): 
  time.sleep(input)
  print(input, os.getpid(), os.getppid(), call([]))

if __name__ == '__main__':
    arr = [1,2,1,2,1,2,1,2,1,2]
    with Timer() as t:
      with Pool(5) as p:
          p.map(do_something, arr)
          p.close() 
          p.join()
    print(t.secs)