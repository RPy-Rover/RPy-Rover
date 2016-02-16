# -*- coding: utf-8 -*-
# =================================================================
#                     EURO RPY-ROVER PROJECT
#                     rpyrover.wordpress.com
# =================================================================
#        File: R_Camera.py v1.0
# =================================================================
#     Runs in: Rover (RPi)
# Required HW: Picamera
# =================================================================
# Copyright (C) 2015  Pedro Tavares / Gil Tavares / André Tavares
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License

import time
import picamera

# Takes photo with dimensions given in the parameters and stores in file with name equal to date/time
def cmd_take_photo(width,height):
    photo_name = time.strftime('%c') + '.png'
    with picamera.PiCamera() as camera:
	camera.resolution = (width,height)
        camera.capture(photo_name)
    return (photo_name)
