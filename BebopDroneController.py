from pyparrot.Bebop import Bebop
# msvcrt is a windows specific native module
import msvcrt
import time


# checks if a key has been hit
def kbfunc():
    if msvcrt.kbhit():  # boolean for if keyboard has been hit
        return msvcrt.getch()  # returns character encoded in binary ASCII
    else:
        return False


bebop = Bebop()
print("Trying to connect...")
success = bebop.connect(10) # attempts to connect to the drone, success is Boolean
if success:
    print("Successfully Connected to Bebop drone!")
    print("Sleeping")
    bebop.smart_sleep(3)
    print("Ready!")
    bebop.ask_for_state_update()
    takeoff = False
    while True:
        # acquire the keyboard hit if exists
        x = kbfunc()

        if x:  # if we got a keyboard hit
            print(x.decode(), end='')  # temp
            if x == chr(27).encode():  # 'ESC' key to exit program
                print("STOPPING")
                success = bebop.disconnect()
                print("Drone "+success+" to disconnect.")
                exit()
            elif x.decode() == 't':
                if takeoff:
                    print("Drone already took off!")
                else:
                    print("Drone taking off...")
                    bebop.safe_takeoff(5)
                    takeoff = True
            elif x.decode() == 'l':
                if takeoff:
                    print("Drone landing...")
                    bebop.safe_land(5)
                    takeoff = False
                else:
                    print("Drone already landed.")
            elif takeoff:
                if x.decode() == 'w':  # by default decodes to utf-8
                    print("fly forwards")
                    print("flying state is %s" % bebop.sensors.flying_state)
                    success = bebop.fly_direct(roll=0, pitch=50, yaw=0, vertical_movement=0, duration=1)
                    print("mambo directional control result is: %s" % success)
                    bebop.smart_sleep(2)
                elif x.decode() == 'a':
                    print("tilt left")
                    print("flying state is %s" % bebop.sensors.flying_state)
                    success = bebop.fly_direct(roll=-50, pitch=0, yaw=0, vertical_movement=0, duration=1)
                    print("mambo directional control result is: %s" % success)
                    bebop.smart_sleep(2)
                elif x.decode() == 's':
                    print("fly backwards")
                    print("flying state is %s" % bebop.sensors.flying_state)
                    success = bebop.fly_direct(roll=0, pitch=-50, yaw=0, vertical_movement=0, duration=1)
                    success = bebop.fly_direct()
                    print("mambo directional control result is: %s" % success)
                    bebop.smart_sleep(2)
                elif x.decode() == 'd':
                    print("tilt right")
                    print("flying state is %s" % bebop.sensors.flying_state)
                    success = bebop.fly_direct(roll=50, pitch=0, yaw=0, vertical_movement=0, duration=1)
                    print("mambo directional control result is: %s" % success)
                    bebop.smart_sleep(2)
                elif x.decode() == 'q':
                    print("ascend")
                    print("flying state is %s" % bebop.sensors.flying_state)
                    success = bebop.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=50, duration=1)
                    print("mambo directional control result is: %s" % success)
                    bebop.smart_sleep(2)
                elif x.decode() == 'e':
                    print("descend")
                    print("flying state is %s" % bebop.sensors.flying_state)
                    success = bebop.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=-50, duration=1)
                    print("mambo directional control result is: %s" % success)
                    bebop.smart_sleep(2)
            else:
                if x.decode() in 'wasd':
                    print("Drone landed, please takeoff first!")
        else:
            # wait half a second
            time.sleep(0.5)
else:
    print("Could not connect to a drone.")

