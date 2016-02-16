# -*- coding: utf-8 -*-
# =================================================================
#                     EURO RPY-ROVER PROJECT
#                     rpyrover.wordpress.com
# =================================================================
#        File: R_Ranger.py
# =================================================================
#     Runs in: Rover (RPi)
# Required HW: Pololu Carrier with Sharp GP2Y0A60SZLF Analog
#               Distance Sensor 10-150cm, 3V
#              MCP3008 SPI ADC
# =================================================================
# Copyright (C) 2015  Pedro Tavares / Gil Tavares / André Tavares
#
# Includes SPI ADC reading code by Scruss (thanks!)
# http://scruss.com/blog/2013/02/02/simple-adc-with-the-raspberry-pi/
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License

import spidev
import time
 
def obstacle_present():
    spi = spidev.SpiDev()# Create object
    spi.open(0, 0)# Open SPI port 0 on (CS) 0
    adcaverage = 0
    for averagenum in range(0,100):           
        r = spi.xfer2([1, 8 + 0 << 4, 0])
        adcout = ((r[1] & 3) << 8) + r[2]
        adcaverage += adcout
    adcaverage = adcaverage/100
    if adcaverage >= 300:
        spi.close()
        return 1
    else:
        spi.close()
        return 0
