from multiprocessing import Pool 
from timer import Timer
import time

def do_something(input): 
  time.sleep(1)
  print(input)

if __name__ == '__main__':
    with Timer() as t:
        for i in range(10): 
            do_something(i)
    print(t.secs)