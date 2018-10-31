from pyparrot.Bebop import Bebop
# msvcrt is a windows specific native module
import msvcrt
import time


bebopAddr = "MAC ADDRESS HERE"  # todo

bebop = Bebop()

print("Trying to connect...")
success = bebop.connect(10)
print(success)

print("Sleeping")
bebop.smart_sleep(5)

bebop.ask_for_state_update()j

if success:
    '''
    bebop.safe_takeoff(10)

    print("flip left")
    print("flying state is %s" % bebop.sensors.flying_state)
    success = bebop.flip(direction="left")
    print("mambo flip result %s" % success)
    bebop.smart_sleep(5)

    print("flip right")
    print("flying state is %s" % bebop.sensors.flying_state)
    success = bebop.flip(direction="right")
    print("mambo flip result %s" % success)
    bebop.smart_sleep(5)

    print("flip front")
    print("flying state is %s" % bebop.sensors.flying_state)
    success = bebop.flip(direction="front")
    print("mambo flip result %s" % success)
    bebop.smart_sleep(5)

    print("flip back")
    print("flying state is %s" % bebop.sensors.flying_state)
    success = bebop.flip(direction="back")
    print("mambo flip result %s" % success)
    bebop.smart_sleep(5)

    bebop.smart_sleep(5)
    bebop.safe_land(10)

    print("DONE - disconnecting")
    bebop.disconnect()
    '''


# asks whether a key has been acquired
def kbfunc():
    #this is boolean for whether the keyboard has bene hit
    x = msvcrt.kbhit()
    if x:
        #getch acquires the character encoded in binary ASCII
        ret = msvcrt.getch()
    else:
        ret = False
    return ret

#begin the counter
number = 1

#infinite loop
while True:

    #acquire the keyboard hit if exists
    x = kbfunc()

    #if we got a keyboard hit
    if x != False and x.decode() == 's':
        #we got the key!
        #because x is a binary, we need to decode to string
        #use the decode() which is part of the binary object
        #by default, decodes via utf8
        #concatenation auto adds a space in between
        print ("STOPPING, KEY:", x.decode())
        #break loop
        break
    else:
        #prints the number
        print (number)
        #increment, there's no ++ in python
        number += 1
        #wait half a second
        time.sleep(0.5)