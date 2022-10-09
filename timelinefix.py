#This may cause a blue light to shoot out of your computer, in case of antimatter creation at point of matter, causing a gamma ray burst followed by memory error
#Which numbers you land at determine what side, thread and dimension were stopped at, followed by a check of if it matches the stored data. If stored data is uncertain it was stopped between dimensions.
print("Usage Python3 timelinefix.py \"problem\" \"fix\"")
print("ctrl+c to stop the roulette wheel, if matched thats what timeline, side and thread you're in")
print("if not matched, you've switched timelines during times flow backwards")
print("if caught between two, the dimensions are uncertain")

import threading
import signal
import sys
store = ""
store1 = ""
store2 = ""
store3 = ""
def sigint_handler(signal, frame):
    global store
    global store1
    global store2
    global store3
    print("")
    if str(store) == "" or str(store1) == "" or str(store2) == "" or str(store3) == "":
        print("Uncertainty Multiverse")
    else:
        print(str(store)+"----"+str(store1)+" "+str(store2)+" "+str(store3))
    sys.exit(0)
signal.signal(signal.SIGINT, sigint_handler)

def electron(currentposition, lastposition, start, dend):
        global store
        global store1
        currentposition = start
        lastposition = dend
        while True:
                
                print(start, end="\r", flush=True)
                currentposition = lastposition
                lastposition = currentposition
                print(" -----"+str(dend), end="\r", flush=True)
                store = start
                store1 = lastposition
def electron2(currentposition, lastposition, start, dend):
        global store
        global store1
        currentposition = start
        lastposition = dend
        while True:
                
                print(start, end="\r", flush=True)
                lastposition = currentposition
                currentposition = lastposition
                print(" -----"+str(dend), end="\r", flush=True)
                store = start
                store1 = lastposition
def knot(dimension):
        global store2
        global store3
        t1 = threading.Thread(target=electron, args=(sys.argv[1],sys.argv[2],1,2))
        t2 = threading.Thread(target=electron2, args=(sys.argv[1],sys.argv[2],3,4))
        t3 = threading.Thread(target=electron, args=(sys.argv[1],sys.argv[2],5,6))
        t4 = threading.Thread(target=electron2, args=(sys.argv[1],sys.argv[2],7,8))
        t1.start()
        t2.start()
        t3.start()
        t4.start()
        def func1():
                global store2
                while True:
                        t1 = t4
                        print("         t1-t4  ", end="\r", flush=True)
                        store2 = "t1-t4"
                        t2 = t3
                        print("         t2-t3  ", end="\r", flush=True)
                        store2 = "t2-t3"
        def func2():
                global store3
                while True:
                        t3 = t2
                        print("         t3-t2  ", end="\r", flush=True)
                        store2 = "t3-t2"
                        t4 = t1
                        print("         t4-t1  ", end="\r", flush=True)
                        store2 = "t4-t1"
                        print("                "+dimension, end="\r", flush=True)
                        store3 = dimension
        t9 = threading.Thread(target=func1)
        t10 = threading.Thread(target=func2)
        t9.start()
        t10.start()
        t9.join()
        t10.join()
        t1.join()
        t2.join()
        t3.join()
        t4.join()

if __name__ =="__main__":
        t5 = threading.Thread(target=knot, args=("timeline 1",))
        t6 = threading.Thread(target=knot, args=("timeline 2",))
        t7 = threading.Thread(target=knot, args=("timeline 3",))
        t8 = threading.Thread(target=knot, args=("timeline 4",))
        t5.start()
        t6.start()
        t7.start()
        t8.start()
        t5.join()
        t6.join()
        t7.join()
        t8.join()

