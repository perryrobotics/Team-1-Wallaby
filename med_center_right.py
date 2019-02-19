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
 	arm_down(STANDARD_STEP)
  	claw_open(STANDARD_STEP)
  	#SCORED FIRETRUCK, NOW GET FIRST FIREMAN
  	arm_up(STANDARD_STEP)
 	left(900, 300)
  	backward(900, 6000)
  	right(900, 300)
  	backward(900, 1000) #Hit Pipe
   	forward(900, 1200)
   	left(900, 800)
  	move_to_black(900, 0, 3000)
	arm_down(STANDARD_STEP)
   	forward(900, 300)
   	msleep(500)

   	right(600, 500)
  	claw_close(STANDARD_STEP)
   	arm_up(STANDARD_STEP)
   	forward(900, 1000)
   	right(900,300)
   	move_to_black(900, 0, 3000)
  	forward(900,1000)
  	move_to_black(900, 0, 3000)
  	arm_down(STANDARD_STEP)
  	claw_open(STANDARD_STEP)
  	arm_up(STANDARD_STEP)
  	#GO SCORE FIREMAN #2!!!
 	left(900, 300)
  	backward(900, 6000)
  	right(900, 300)
  	backward(900, 1000) #Hit Pipe
   	forward(900, 1200)
   	left(900, 800)
  	move_to_black(900, 0, 3000)
	arm_down(STANDARD_STEP)
   	forward(900, 300)
   	msleep(500)

   	right(600, 500)
  	claw_close(STANDARD_STEP)
   	arm_up(STANDARD_STEP)
   	forward(900, 1000)
   	right(900,300)
   	move_to_black(900, 0, 3000)
  	forward(900,1000)
  	move_to_black(900, 0, 3000)
  	arm_down(STANDARD_STEP)
  	claw_open(STANDARD_STEP)
  	arm_up(STANDARD_STEP) 
  	#FIREMAN 2 SCORED!  GET #3!!
  	left(900, 300)
  	backward(900, 6000)
  	right(900, 300)
  	backward(900, 1000) #Hit Pipe
   	forward(900, 1200)
   	left(900, 800)
  	move_to_black(900, 0, 3000)
	arm_down(STANDARD_STEP)
   	forward(900, 300)
   	msleep(500)

   	right(600, 500)
  	claw_close(STANDARD_STEP)
   	arm_up(STANDARD_STEP)
   	forward(900, 1000)
   	right(900,300)
   	move_to_black(900, 0, 3000)
  	forward(900,1000)
  	move_to_black(900, 0, 3000)
  	arm_down(STANDARD_STEP)
  	claw_open(STANDARD_STEP)
  	arm_up(STANDARD_STEP)        
    #FIREMAN 3 SCORED!  GET #4!!
  	left(900, 300)
  	backward(900, 6000)
  	right(900, 300)
  	backward(900, 1000) #Hit Pipe
   	forward(900, 1200)
   	left(900, 800)
  	move_to_black(900, 0, 3000)
	arm_down(STANDARD_STEP)
   	forward(900, 300)
   	msleep(500)

   	right(600, 500)
  	claw_close(STANDARD_STEP)
   	arm_up(STANDARD_STEP)
   	forward(900, 1000)
   	right(900,300)
   	move_to_black(900, 0, 3000)
  	forward(900,1000)
  	move_to_black(900, 0, 3000)
  	right(900, 450)
  	arm_down(STANDARD_STEP)
   	left(900,500)
  	claw_open(STANDARD_STEP)
        
  	arm_up(STANDARD_STEP)
        