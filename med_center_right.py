#!/usr/bin/python
import os, sys
from wallaby import *     
from movement import * 
from effectors import *

def medical_center_right():
	print "medical_center_right"
	move_to_white(900,0,3000)
  	forward(900,500)
	right(900,300) 
	move_to_black(900,0,3000)
 	left(900, 50)#turn to keep it im the sttart box
 	arm_down(50)
  	claw_open(STANDARD_STEP)
        
        
  	#========================================================================
  	#SCORED FIRETRUCK, NOW GET FIRST FIREMAN	
	#========================================================================
  	arm_up(STANDARD_STEP)
 	#right(900, 100)
 	left(900, 100)
  	backward(900, 2000)
  	right(900, 350)
  	backward(900,5000)  #hit back of pipe!!
 	for cube in range(4):
		forward(900, 830)  #forward to get even with fireman
		left(900,900) #face fireman
		move_to_black(900, 0, 2700)
		arm_fireman(50)  # start to grab first fireman
		forward(800, 380) #go forward to grab fireman
		msleep(500)

		right(600, 500)
		claw_close(STANDARD_STEP) #grabbed first fireman!!!
		arm_su(STANDARD_STEP)
		forward(900, 1000)
		right(900,45)
		move_to_black(900, 0, 3000)
		forward(900,1500)#forward to scoreing zone
       
		#move_to_black(900, 0, 3000)
		#arm_down(STANDARD_STEP)
		claw_half(50)
		arm_up(STANDARD_STEP)
		claw_open(STANDARD_STEP)
		#========================================================================
		#SCORED FIRETRUCK, NOW GET SECOND FIREMAN	
		#========================================================================
		if cube == 3:
			print "BREAK LOOP!!!"
			break
		left(900, 300)
		backward(900, 3500)
		right(900, 200) #correction tutn
		backward(900, 3500) #Hit Pipe
	#backward(900, 1000)
	right(900, 500)
	arm_down(STANDARD_STEP)
	forward(900, 2000)
	left(900, 1000)
	forward(900, 2000)
