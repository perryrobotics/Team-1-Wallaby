#!/usr/bin/python
import os, sys
from wallaby import *     
from movement import * 
 
ARM_P = 0
ARM_D = 1600
ARM_U = 500
ARM_B = 50
ARM_F = 1650
ARM_SU =1550
ARM_DROP_F = 975

CLAW_P = 2
CLAW_O = 1100
CLAW_C = 500
CLAW_H = 800
STANDARD_STEP = 100

def move_servo_slow(port, start_pos, end_pos, step):
	if start_pos > end_pos:
		step = -step
	for pos in range(start_pos, end_pos, step):
		#print pos
		set_servo_position(port, pos)
 		msleep(25)
	set_servo_position(port, end_pos)
            
def arm_down(step):
	move_servo_slow(ARM_P, ARM_U, ARM_D, step)
        
def arm_up(step):
	move_servo_slow(ARM_P, ARM_D, ARM_U, step)  
        
def arm_back(step):
	move_servo_slow(ARM_P, ARM_D, ARM_B, step)

def arm_su(step):
	move_servo_slow(ARM_P, ARM_D, ARM_SU, step)
        
        
def arm_fireman(step):
	move_servo_slow(ARM_P, ARM_U, ARM_F, step)

def arm_drop_fireman(step):
	move_servo_slow(ARM_P, ARM_U, ARM_DROP_F, step)
        
def claw_open(step):
	move_servo_slow(CLAW_P, CLAW_C, CLAW_O, step)
        
def claw_close(step):
	move_servo_slow(CLAW_P, CLAW_O, CLAW_C, step)

def claw_half(step):
	move_servo_slow(CLAW_P, CLAW_C, CLAW_H, step)

