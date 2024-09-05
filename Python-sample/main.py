
import logging
import os
import pyroscope

l = logging.getLogger()
l.setLevel(logging.DEBUG)

#addr = os.getenv("PYROSCOPE_SERVER_ADDRESS")
#print(addr)

pyroscope.configure(
 
        application_name    = "simple.python.app",
        server_address      = "pyroscope-server:4040",
        enable_logging      = True,
        sample_rate         = 100
       # detect_subprocesses = False,
        #oncpu               = True,
        #gil_only            = True

)

def work(n):
 i = 0
 while i < n:
  i += 1

def fast_function():
 with pyroscope.tag_wrapper({ "function": "fast" }):
  work(20000)

def slow_function():
 with pyroscope.tag_wrapper({ "function": "slow" }):
     work(80000)

if __name__ == "__main__":
 while True:
  fast_function()
  slow_function()