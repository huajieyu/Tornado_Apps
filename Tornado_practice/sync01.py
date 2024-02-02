import os, sys
import time

def longIo():
    print("beginning of the time consuming")
    time.sleep(5)
    print("end of time consuming")
    return ("LongIo is a function for test")

def reqA():
    print("Start of Process A")
    res=longIo()
    print("received longIo response data: ", res)
    print("End of process A")

def reqB():
    print("Start of Process B")
    print("End of process B")

# in asynchronous process, the time consuming process 
# is taken by another thread
# 1, call back function
#
# 2. coroutine
#
#
#
#

# similar to the service in Tornado
def main():
    reqA()
    reqB()
    while 1:
        time.sleep(0.1)
        pass

if __name__ =="__main__":
    main()
    sys.exit(0)
