import concurrent.futures
from timer import Timer
import time
import os

def do_something(input): 
  time.sleep(input)
  return (input, os.getpid(), os.getppid())

if __name__ == '__main__':
    arr = [1,2,1,2,1,2,1,50,1,2]
    with Timer() as t:
      with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
          for i in zip(executor.map(do_something, arr)):
              print(i)
    print(t.secs)