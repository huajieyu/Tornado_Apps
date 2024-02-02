import os
import time
import threading
import sys
gen=None

def longIo():
    def run():
        print("beginning of the time consuming")
        time.sleep(5)
        print("end of time consuming")
        try: 
            global gen
            gen.send("response from the LongIo time consuming ")
        except StopIteration as e:
            pass 
    threading.Thread(target=run).start()

# call back function
def finish(data):
    print("start processing callback function")
    print("received LongIo response data: ", data)
    print("end of processing callback function")

# create a decorator
def genCoroutine(func):
    def wrapper(*args, **kwargs):
        global gen
        gen=func(*args, **kwargs)
        next(gen)
        
    return wrapper
    # decorator returned function no parathesis

@genCoroutine
def reqA():
    print("Start of Process A")
    # use yield
    res = yield longIo()
    print("get the response of longIo function: ", res)
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
    # condition 2 use a decorator
    reqA()
    reqB()
    # sleep means let the function give up using the CPU instead of
    # CPU wait for very long time
    while True:
        time.sleep(0.1)
        pass

if __name__ =="__main__":
    main()
    # sys.exit(0)

