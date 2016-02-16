# -*- coding: utf-8 -*-
# =================================================================
#                     EURO RPY-ROVER PROJECT
#                     rpyrover.wordpress.com
# =================================================================
#        File: R_Motors.py
# =================================================================
#     Runs in: Rover (RPi)
# Required HW: 2 LEDs
#	       +
#	       Dagu Rover 5 Tracked Chassis with Encoders
#              +
#              Pololu Qik 2s9v1 Dual Serial Motor Controller
# =================================================================
# Copyright (C) 2015  Pedro Tavares / Gil Tavares / André Tavares
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License


import wiringpi2 as wp
import R_Ranger
import math
import subprocess
import time
argument = ''
proc = 0
rpi = 0
MAXSPEED = 127
PAUSE = 0.16
ROTATIONPAUSE = 0.115
wp.wiringPiSetup()

def blinkon():
    global proc
    proc = subprocess.Popen(['python', '.py', argument], shell=False)

def blinkoff():
    proc.terminate()
    wp.digitalWrite(7,0)

# Open serial port ------------------------------------
def open_serial_port():
    global rpi
    rpi = wp.serialOpen("/dev/ttyAMA0",38400)
    wp.serialPutchar(rpi,170)

def close_serial_port():
    wp.serialClose(rpi)

def cmd_forward():
    open_serial_port()
    blinkon()
    for t in range(0,21):
        message = [0x88,int(math.floor(t*MAXSPEED/20)),0x8c,int(math.floor(t*MAXSPEED/20))]
        for a in range(0,4):
            wp.serialPutchar(rpi,(message[a]))
        if R_Ranger.obstacle_present() == 1:
            message = [0x88,0,0x8c,0]
            for a in range(0,4):
                wp.serialPutchar(rpi, message[a])
            close_serial_port()
            return -1
        time.sleep(PAUSE)
    for t in range(20,-1, -1):
        message = [0x88,int(math.floor(t*MAXSPEED/20)),0x8c,int(math.floor(t*MAXSPEED/20))]
        for a in range(0,4):
            wp.serialPutchar(rpi, message[a])
        if R_Ranger.obstacle_present() == 1:
            message = [0x88,0,0x8c,0]
            for a in range(0,4):
                wp.serialPutchar(rpi, message[a])
            close_serial_port()
            return -1
        time.sleep(PAUSE)
    blinkoff()
    close_serial_port()
    return 0

def cmd_reverse():
    open_serial_port()
    blinkon()
    for t in range(0,21):
        message = [0x8a,int(math.floor(t*MAXSPEED/20)),0x8e,int(math.floor(t*MAXSPEED/20))]
        for a in range(0,4):
            wp.serialPutchar(rpi, message[a])
        time.sleep(0.1)
    for t in range(20,-1,-1):
        message = [0x8a,int(math.floor(t*MAXSPEED/20)),0x8e,(math.floor(t*MAXSPEED/20))]
        for a in range(0,4):
            wp.serialPutchar(rpi, message[a])
        time.sleep(0.1)
    blinkoff()
    close_serial_port()
        
def cmd_rotateright():
    open_serial_port()
    blinkon()
    for t in range(0,21):
        message = [0x8a,int(math.floor(t*MAXSPEED/20)),0x8c,int(math.floor(t*MAXSPEED/20))]
        for a in range(0,4):
            wp.serialPutchar(rpi, message[a])
        time.sleep(ROTATIONPAUSE)
    for t in range(20,-1,-1):
        message = [0x8a,int(math.floor(t*MAXSPEED/20)),0x8c,int(math.floor(t*MAXSPEED/20))]
        for a in range(0,4):
            wp.serialPutchar(rpi, message[a])
        time.sleep(ROTATIONPAUSE)
    blinkoff()
    close_serial_port()

def cmd_rotateleft():
    open_serial_port()
    blinkon()
    for t in range(0,21):
        message = [0x88,int(math.floor(t*MAXSPEED/20)),0x8e,int(math.floor(t*MAXSPEED/20))]
        for a in range(0,4):
            wp.serialPutchar(rpi, message[a])
        time.sleep(ROTATIONPAUSE)
    for t in range(20,-1,-1):
        message = [0x88,int(math.floor(t*MAXSPEED/20)),0x8e,int(math.floor(t*MAXSPEED/20))]
        for a in range(0,4):
            wp.serialPutchar(rpi, message[a])
        time.sleep(ROTATIONPAUSE)
    blinkoff()
    close_serial_port()
