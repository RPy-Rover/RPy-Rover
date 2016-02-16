# -*- coding: utf-8 -*-
# =================================================================
#                     EURO RPY-ROVER PROJECT
#                     rpyrover.wordpress.com
# =================================================================
#        File: R_GPS.py
# =================================================================
#     Runs in: Rover (RPi)
# Required HW: 66-Channel LS20031 GPS Receiver Module
#              (MT3339 Chipset)
# =================================================================
# Copyright (C) 2015  Pedro Tavares / Gil Tavares / André Tavares
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License


import wiringpi2 as wp

# return RMC string

def getrmc():

    serial = wp.serialOpen("/dev/ttyAMA0",57600) # open serial port 

    wp.serialFlush(serial)
    print(serial)
    while True: # repeat until we get a RMC NMEA string
        gpsstring = ""
        while True: # repeat until we have a complete string
            if (wp.serialDataAvail(serial) > 0):
		letter = wp.serialGetchar(serial)
                if letter == 10:
                    break
	        else:
                    gpsstring += str(chr(letter))
        if (gpsstring[3:6]=="RMC"):
           break
    wp.serialClose(serial)
    return(gpsstring)


def cmd_read_GPS():
    reading=getrmc()
    # determine the position of the value separating commas
    commas = [0,1,2,3,4,5,6,7,8,9,10,11]
    comnum = 0
    for i in range (0,len(reading)):
        if reading[i] == ",":
            commas[comnum] = i # save the position of the comma
            comnum += 1
    # Extract latitude
    if (reading[commas[3] + 1:commas[4]]) == "N":
        sign = 1
    else:
        sign = -1

    degrees = float(reading[commas[2]+1:commas[2]+3])
    minutes = float(reading[commas[2] + 3:commas[3]])/60
    latitude = sign*(degrees + minutes)
    # Extract Longitude
    if (reading[commas[5] + 1:commas[6]]) == "E":
        sign = 1
    else:
        sign = -1

    degrees = float(reading[commas[4]+1:commas[4]+3])
    minutes = float(reading[commas[4] + 3:commas[5]])/60
    longitude = sign*(degrees + minutes)
    

    return(str(latitude),",",str(longitude))

