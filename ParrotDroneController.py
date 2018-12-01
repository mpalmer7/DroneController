from pyparrot.Bebop import Bebop
from pyparrot.Minidrone import Mambo
# msvcrt is a windows specific native module
import msvcrt
import time

# checks if a key has been hit
def kbfunc():
    if msvcrt.kbhit():  # boolean for if keyboard has been hit
        return msvcrt.getch()  # returns character encoded in binary ASCII
    else:
        return False

def controller(drone):
	takeoff = False
	while True:
		# acquire the keyboard hit if exists
		x = kbfunc()

		if x:  # if we got a keyboard hit
			print(x.decode(), end='')  # temp
			if x == chr(27).encode():  # 'ESC' key to exit program
				print("STOPPING")
				success = drone.disconnect()
				print("Drone %s to disconnect." % success)
				exit()
			elif x.decode() == 't':
				if takeoff:
					print("Drone already took off!")
				else:
					print("Drone taking off...")
					success = drone.safe_takeoff(5)
					print("Drone %s to take off!" % success)
					takeoff = True
			elif x.decode() == 'l':
				if takeoff:
					print("Drone landing...")
					success = drone.safe_land(5)
					print("Drone %s to land!" % success)
					takeoff = False
				else:
					print("Drone already landed.")
			elif takeoff:
				if x.decode() == 'w':  # by default decodes to utf-8
					print("fly forwards")
					print("flying state is %s" % drone.sensors.flying_state)
					success = drone.fly_direct(roll=0, pitch=50, yaw=0, vertical_movement=0, duration=1)
					print("mambo directional control result is: %s" % success)
					drone.smart_sleep(1)
				elif x.decode() == 'a':
					print("tilt left")
					print("flying state is %s" % drone.sensors.flying_state)
					success = drone.fly_direct(roll=-50, pitch=0, yaw=0, vertical_movement=0, duration=1)
					print("mambo directional control result is: %s" % success)
					drone.smart_sleep(1)
				elif x.decode() == 's':
					print("fly backwards")
					print("flying state is %s" % drone.sensors.flying_state)
					success = drone.fly_direct(roll=0, pitch=-50, yaw=0, vertical_movement=0, duration=1)
					print("mambo directional control result is: %s" % success)
					drone.smart_sleep(2)
				elif x.decode() == 'd':
					print("tilt right")
					print("flying state is %s" % drone.sensors.flying_state)
					success = drone.fly_direct(roll=50, pitch=0, yaw=0, vertical_movement=0, duration=1)
					print("mambo directional control result is: %s" % success)
					drone.smart_sleep(1)
				elif x.decode() == 'q':
					print("ascend")
					print("flying state is %s" % drone.sensors.flying_state)
					success = drone.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=50, duration=1)
					print("mambo directional control result is: %s" % success)
					drone.smart_sleep(1)
				elif x.decode() == 'e':
					print("descend")
					print("flying state is %s" % drone.sensors.flying_state)
					success = drone.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=-50, duration=1)
					print("mambo directional control result is: %s" % success)
					drone.smart_sleep(1)
			else:
				if x.decode() in 'wasdqe':
					print("Drone landed, please takeoff first!")	
		
		
		
def main():
	bebop2 = Bebop()
	bebop1 = Bebop(drone_type="Bebop")
	mambo = Mambo(mac, use_wifi=True)
	print("Trying to connect...")
	success = bebop.connect(10) # attempts to connect to the drone, success is Boolean
	success = True
	
	print("Successfully Connected to drone!")
	print("Sleeping")
	drone.smart_sleep(3)
	print("Ready!")
	drone.ask_for_state_update()
	
	else:
		print("Could not connect to a drone.")

if __name__ == "__main__":
	main()