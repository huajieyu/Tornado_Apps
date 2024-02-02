import os, sys
import time
import threading

def longIo(callback):
    def run(cb):
        print("beginning of the time consuming")
        time.sleep(5)
        print("end of time consuming")
        cb("longIo response to request test")
    threading.Thread(target=run, args=(callback,)).start()

# call back function
def finish(data):
    print("start processing callback function")
    print("received LongIo response data: ", data)
    print("end of processing callback function")


def reqA():
    print("Start of Process A")
    longIo(finish)
    print("End of process A")

def reqB():
    print("Start of Process B")
    # longIo()
    print("End of process B")

# in asynchronous process, the time consuming process 
# is taken by another thread
# for example ajax request
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
