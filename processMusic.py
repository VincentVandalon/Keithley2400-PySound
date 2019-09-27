#Copyright 2012 Vincent Vandalon
#
#This file is part of <++>. <++> is free software: you can redistribute
#it and/or modify it under the terms of the GNU General Public License
#as published by the Free Software Foundation, either version 3 of the
#License, or (at your option) any later version.
#
#<++> is distributed in the hope that it will be useful, but WITHOUT
#ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
#or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public
#License for more details. You should have received a copy of
#the GNU General Public License along with <++>. If not, see #<http://www.gnu.org/licenses/>. " 
 
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import sys
reload(sys)  
sys.setdefaultencoding('utf-8')

import matplotlib as mpl
mpl.rc('lines', linewidth=2,markersize=10)
mpl.rc('font', size=16)

import time
#pip install pyserial
import serial

def pitch(strg):
    strg = strg.replace('S','#')
    lookup = {
    "C0":16.35, "C#0":17.32, "D0":18.35, "D#0":19.45, "E0":20.60,
    "F0":21.83, "F#0":23.12, "G0":24.50, "G#0":25.96, "A0":27.50,
    "A#0":29.14, "B0":30.87, "C1":32.70, "C#1":34.65, "D1":36.71,
    "D#1":38.89, "E1":41.20, "F1":43.65, "F#1":46.25, "G1":49.00,
    "G#1":51.91, "A1":55.00, "A#1":58.27, "B1":61.74, "C2":65.41,
    "C#2":69.30, "D2":73.42, "D#2":77.78, "E2":82.41, "F2":87.31,
    "F#2":92.50, "G2":98.00, "G#2":103.83, "A2":110.00, "A#2":116.54,
    "B2":123.47, "C3":130.81, "C#3":138.59, "D3":146.83, "D#3":155.56,
    "E3":164.81, "F3":174.61, "F#3":185.00, "G3":196.00, "G#3":207.65,
    "A3":220.00, "A#3":233.08, "B3":246.94, "C4":261.63, "C#4":277.18,
    "D4":293.66, "D#4":311.13, "E4":329.63, "F4":349.23, "F#4":369.99,
    "G4":392.00, "G#4":415.30, "A4":440.00, "A#4":466.16, "B4":493.88,
    "C5":523.25, "C#5":554.37, "D5":587.33, "D#5":622.25, "E5":659.25,
    "F5":698.46, "F#5":739.99, "G5":783.99, "G#5":830.61, "A5":880.00,
    "A#5":932.33, "B5":987.77, "C6":1046.50, "C#6":1108.73, "D6":1174.66,
    "D#6":1244.51, "E6":1318.51, "F6":1396.91, "F#6":1479.98,
    "G6":1567.98, "G#6":1661.22, "A6":1760.00, "A#6":1864.66,
    "B6":1975.53, "C7":2093.00, "C#7":2217.46, "D7":2349.32,
    "D#7":2489.02, "E7":2637.02, "F7":2793.83, "F#7":2959.96, "G7":3135.96,
    "G#7":3322.44, "A7":3520.00, "A#7":3729.31, "B7":3951.07,
    "C8":4186.01, "C#8":4434.92, "D8":4698.63, "D#8":4978.03,
    "E8":5274.04, "F8":5587.65, "F#8":5919.91, "G8":6271.93,
    "G#8":6644.88, "A8":7040.00, "A#8":7458.62, "B8":7902.13,
    "res":0,"0":0,
    }
    return lookup[strg[0:3]]

def makeMusic(notes,counts,tempo=10.,timeInverted=False):

    # configure the serial connections (the parameters differs on the device you are connecting to)
    ser = serial.Serial(
        port='/dev/ttyUSB1',
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS
    )
    ser.isOpen()
    for note,count in zip(notes,counts):
        if timeInverted == True:
            noteDuration = tempo*count/200.
        else:
            noteDuration = tempo*1./count
        if pitch(note) != 0:
            ser.write(":SYST:BEEP:IMM %i, %.2f\n"%(pitch(note),noteDuration))
            print ":SYST:BEEP:IMM %i, %.2f"%(pitch(note),noteDuration)
        time.sleep(1.3*noteDuration)
    #ser.close()

from mario import notes,counts
makeMusic(notes,counts,tempo=1.3)
time.sleep(5)
from imperialMarch import notes,counts
makeMusic(notes,counts,tempo=8,timeInverted=True)
time.sleep(5)
from pirates import notes,counts
makeMusic(notes,counts,tempo=.15,timeInverted=True)
time.sleep(5)
from furElise  import notes,counts
makeMusic(notes,counts,tempo=1.6)
