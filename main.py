#!/usr/bin/python
import os, sys
from wallaby import * 
from movement import * 
from effectors import *
from wait_for_start import *

LEFT = 0
RIGHT = 1
LIGHT_SENSOR = 1
def main():
	enable_servos()
#Get ready for the starting
	msleep(300)
	arm_back(50)
	wait_for_start(LIGHT_SENSOR)
	arm_up(50)
	msleep(15000)
	right(900,1800)
	forward(900,2555)
	move_to_black(900,0,2700)
   	left(900,650)
 	backward(900,1700) # hit pipe
  	forward(900,1000)  #get off pipe
  	right(900,250)
	forward(900,2000)
   	move_to_black(900,0,3000) #go to black tape
    
 	forward(900,3000)    
	right(900,700)  #might_need_to_adjust_at_comp.
	arm_down(50)
 	move_to_black(900,0,2700)
	forward(900,700)
	arm_powerline_1(50)
 	forward(900,350) #changed
	right(500,20)
 	forward(900,900) # might need to adjust
	right(500,195)
	msleep(1000)
	left(900,85)
	backward(900,800)
 	set_servo_position(ARM_P, ARM_D)
	msleep(1000)
	backward(900,2000)
	right(900,100)
	backward(900,2500)
	forward(900,500)
	right(900,50)
	forward(900,3500)
	left(900,1300)  #might_need_to_adjust_at_comp.
	arm_down(50)
	forward(900,2400)
 	arm_power(50)
	msleep(1000)
  	left(300,300)
 	forward(900,900)
	right(900,100)
	msleep(1000)
	left(900,20)
	backward(900,700)
 	set_servo_position(ARM_P, ARM_D)
	msleep(1000)
	backward(900,1000)
	arm_up(50)
	disable_servos()
	
if __name__== "__main__":
	sys.stdout = os.fdopen(sys.stdout.fileno(),"w",0)
	main();
