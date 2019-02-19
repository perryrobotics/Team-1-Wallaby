#!/usr/bin/python
import os, sys
from wallaby import *     
from movement import * 
from effectors import *
from med_center_left import *
from med_center_right import *

LEFT = 0
RIGHT = 1
    
def main():
	enable_servos()
        
#GET INTO STARTING BOX POSITION!
  	arm_back(50)
  	claw_open(50)
  	msleep(5000)
#GO SCORE FIRETRUCK
 	shut_down_in(120)
        
	backward_time(100, 1000) # go hit against start box pipe
  	forward(900, 500)
    #forward_time(100, 500) #go forward 
  	left(900, 900) #turn to left side of start box
    #The next three instructions move the robot to the black tape
   	#then to the white and then all the way to the firstation black tabe
  	move_to_black(900, 0, 2700)
  	move_to_white(900, 0, 500)
  	move_to_black(900, 0, 2700)
        
	 
  	backward_time(900, 1200)  #Back up a bit 
  	right(900, 850) #and turn to face the center of board
	backward_time(900, 750) #Hit the back pipe
  	forward(900, 1000)
   	left(900, 950) #turn to face the firetruck  MIGHT NEED TO ADJUST IN COMP
   	arm_down(50)
  	forward(900, 900)
  	claw_close(50) #GOT FIRETRUCK!!!!
   	msleep(500)
  	arm_up(50)  
    #GOT FIRETRUCK!!!
  	backward(900, 100)
   	right(900,600)   #might need to change this if you change the above left
   	move_to_black(900, 0, 2700)
  	#left(900,100)
 	#CHECK FOR BURNING BUILDING!!
 	left(900,50)  #turn to face building
  	camera_open()
  	side = RIGHT
   	for _ in range(20):
		camera_update()
		num = get_object_count(0)
		if num>0 and get_object_area(0,0) > 4000:
			side = LEFT
		msleep(100)
	if side == LEFT:
		print "LEFT SIDE BURNING!!"
		medical_center_left()
 	else:
		print "RIGHT SIDE BURNING!!"
		medical_center_right()
	

disable_servos()

      



	
    
if __name__== "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(),"w",0)
    main();