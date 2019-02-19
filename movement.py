#!/usr/bin/python
import os, sys
from wallaby import *

DELAY = 100
LMOTOR = 3
RMOTOR = 0
    
def forward(speed, ticks):
	cmpc(RMOTOR)
  	cmpc(LMOTOR)
	#mrp(RMOTOR, speed, ticks)
	#mrp(LMOTOR, speed, ticks)
  	#bmd(LMOTOR)
  	mav(LMOTOR, speed)
  	mav(RMOTOR, speed)
 	while gmpc(LMOTOR) < ticks:
		pass
	ao()
  	msleep(DELAY)
        
def backward(speed, ticks):
	cmpc(RMOTOR)
  	cmpc(LMOTOR)
  	mav(LMOTOR, -speed)
  	mav(RMOTOR, -speed)
	#mrp(RMOTOR, speed, -ticks)
	#mrp(LMOTOR, speed, -ticks)
  	#bmd(LMOTOR)
 	while gmpc(LMOTOR) >-ticks:
		pass
  	ao()  
   	cmpc(RMOTOR)
  	cmpc(LMOTOR)
  	msleep(DELAY)
    
def left(speed, ticks):
	cmpc(RMOTOR)
  	cmpc(LMOTOR)
 	mav(LMOTOR, -speed)
 	mav(RMOTOR, speed)
	#mrp(RMOTOR, speed, ticks)
	#mrp(LMOTOR, speed, -ticks)
  	#bmd(LMOTOR)
  	while gmpc(RMOTOR) < ticks:
		pass
	ao()
   	cmpc(RMOTOR)
  	cmpc(LMOTOR)
 	msleep(DELAY)
        
def right(speed, ticks):
	cmpc(RMOTOR)
  	cmpc(LMOTOR)
  	mav(LMOTOR, speed)
  	mav(RMOTOR, -speed)
	#mrp(RMOTOR, speed, -ticks)
	#mrp(LMOTOR, speed, ticks)
  	#bmd(RMOTOR)
 	while gmpc(LMOTOR) < ticks:
		pass 
	ao()
   	cmpc(RMOTOR)
  	cmpc(LMOTOR)
  	msleep(DELAY)
        
def forward_time(speed, time):
	motor(LMOTOR,  speed)
 	motor(RMOTOR, speed)
  	msleep(time)
 	ao()
  	msleep(DELAY)

def backward_time(speed, time):
	motor(LMOTOR,  -speed)
 	motor(RMOTOR, -speed)
  	msleep(time)
 	ao()
  	msleep(DELAY)

        
def move_to_black(speed, port, thresh): 
	mav(LMOTOR, speed)
  	mav(RMOTOR, speed)
	while analog(port) < thresh:
		pass
	ao()
   	cmpc(RMOTOR)
  	cmpc(LMOTOR)
  	msleep(DELAY)
            
def back_to_black(speed, port, thresh): 
	mav(LMOTOR, -speed)
  	mav(RMOTOR, -speed)
	while analog(port) < thresh:
		pass
 	ao()
 	msleep(DELAY)
            
def move_to_white(speed, port, thresh): 
	mav(LMOTOR, speed)
  	mav(RMOTOR, speed)
	while analog(port) > thresh:
		pass
	ao()
   	cmpc(RMOTOR)
  	cmpc(LMOTOR)
  	msleep(DELAY)