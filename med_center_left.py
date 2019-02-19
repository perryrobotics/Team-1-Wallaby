#!/usr/bin/python
import os, sys
from wallaby import *     
from movement import * 
from effectors import *

def medical_center_left():

	print "medical_center_left"
 	arm_down(50)
 	claw_open(50)  
    #scored firetruck!!
 	arm_up(50)
  	claw_open(10)
        
  	#go get the first fireman!!
  	backward(900,3000) 
   	#backup out of buring buildiung
 	left(900, 350) 
    #Turn to face firepole
   	move_to_black(900, 0, 2700)
        
  	backward(900, 400)
  	right(900, 800)
 	backward(900, 1300) #hit back of pipe
  	forward(900, 950)
  	left(900,900)
  	move_to_black(900, 0, 2700)
  	arm_fireman(50)  # start to grab first fireman
  	forward(800, 275)
   	msleep(1000)
  	right(900, 400)
   	forward(900,50)
  	claw_close(50)
   	arm_up(50)
  	forward(900, 500)
  	move_to_black(900, 0, 2700)
 	#right(900,50)
  	arm_drop_fireman(10) #score first fireman
  	claw_open(10)
  	arm_up(50)
  	backward(900, 1200)
   	#FIRST FIREMAN SCORED NOW SCORING SECOND FIREMAN
  	move_to_black(900, 0, 2700)
   	left(900,450)
  	backward(900, 3000)
 	right(900, 900)
   	backward(1200,3100) # Hits back of pipe.
	forward(900, 1050) # got forward to get inline to get second fireman
  	left(900,1000)
  	move_to_black(900, 0, 2700)
	arm_fireman(50)
  	forward(800, 325)
   	msleep(1000)
  	right(900, 400)
   	forward(900,50)
  	claw_close(50) #gripped second fireman!!!!!
  	forward(800, 50)
  	right(900, 175)
  	forward(800, 500)
 	claw_open(50) #score second fireman!!!
  	arm_up(50)
  	#GO GET THIRD FIREMAN!!!
   	left(500,300)
 	backward(900,1500)
  	right(900, 300)
  	backward(900, 2500) # Hits back of the pipe.
 	forward(900, 950)
  	left(900,930) #turnb to face fireman
  	move_to_black(900, 0, 2700)
	arm_fireman(50)
  	forward(800, 275)
   	claw_close(50)
   	msleep(1000)
  	right(900, 500)
  	forward(900, 500)
  	claw_open(50)  #scoe third
    #GO GET FOURTH FIREMAN!!
  	arm_up(50)
   	left(500,300)
  	backward(900, 1500) 
   	right(900, 400)
   	backward(900, 2700)# Hits back of the pipe.
  	forward(900, 950) #go forward to be in line with fourth cube!
  	left(900,930)
  	move_to_black(900, 0, 2700)
	arm_fireman(50)
  	forward(800, 275)
  	claw_close(50)
   	msleep(1000)
  	right(900, 530)
  	claw_open(50)
  	forward(900, 350)
  	arm_up(50)   
   	#LETS SCORE THE LAST CUBE!!
   	left(500,300)
  	backward(900, 1500) 
   	right(900, 400)
   	backward(900, 2700)# Hits back of the pipe.
  	forward(900, 950) #go forward to be in line with fourth cube!
  	left(900,930)
  	move_to_black(900, 0, 2700)
	arm_fireman(50)
  	forward(800, 275)
  	claw_close(50)
   	msleep(1000)
  	backward(900, 100)
  	right(900, 530)
  	forward(400, 300)
  	claw_open(50)
  	forward(900, 350)
  	arm_up(50)   
   	backward(900, 2100)
 	forward(900,2221)
 	arm_down(50)
  	left(900,200)